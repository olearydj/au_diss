#!/bin/zsh

set -euo pipefail

SRC_ROOT="${SRC_ROOT:-/Volumes/ThunderBay mini}"
DEST_ROOT="${DEST_ROOT:-/Volumes/tbm_archive}"
LOG_DIR="${LOG_DIR:-$HOME/tbm-parallel-logs}"
RSYNC_BIN="${RSYNC_BIN:-/opt/homebrew/bin/rsync}"
CAFFEINATE_BIN="${CAFFEINATE_BIN:-/usr/bin/caffeinate}"

COMMON_ARGS=(
  -aHh
  --info=progress2
  --partial
  --append-verify
  --exclude=.DS_Store
  --exclude=.DocumentRevisions-V100/
  --exclude=.DocumentRevisions-V100-bad-1/
  --exclude=.Spotlight-V100/
  --exclude=.TemporaryItems/
  --exclude=.Trashes/
  --exclude=.com.apple.timemachine.donotpresent
  --exclude=.fseventsd/
  --exclude=.LP_Store/
  --exclude='._*'
)

timestamp="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$LOG_DIR"

if [[ ! -d "$SRC_ROOT" ]]; then
  echo "Source root not found: $SRC_ROOT" >&2
  exit 1
fi

if [[ ! -d "$DEST_ROOT" ]]; then
  echo "Destination root not found: $DEST_ROOT" >&2
  exit 1
fi

if [[ ! -x "$RSYNC_BIN" ]]; then
  echo "rsync binary not found or not executable: $RSYNC_BIN" >&2
  exit 1
fi

start_worker() {
  local name="$1"
  shift

  local log_file="$LOG_DIR/${timestamp}-${name}.log"
  local stdout_file="$LOG_DIR/${timestamp}-${name}.stdout"

  nohup "$CAFFEINATE_BIN" -disu "$RSYNC_BIN" "$@" \
    --log-file="$log_file" \
    > "$stdout_file" 2>&1 &

  local pid=$!
  echo "$name pid=$pid"
  echo "  log:    $log_file"
  echo "  stdout: $stdout_file"
}

echo "Launching ThunderBay -> UNAS parallel copy workers"
echo "  source:      $SRC_ROOT"
echo "  destination: $DEST_ROOT"
echo "  logs:        $LOG_DIR"
echo ""

# Worker 1: likely large media tree, isolated for throughput.
start_worker "photos" \
  "${COMMON_ARGS[@]}" \
  "$SRC_ROOT/Photos/" \
  "$DEST_ROOT/Photos/"

# Worker 2: separate project/archive tree, isolated from Photos.
start_worker "n-space" \
  "${COMMON_ARGS[@]}" \
  "$SRC_ROOT/n-Space/" \
  "$DEST_ROOT/n-Space/"

# Worker 3: remaining meaningful top-level archive content.
start_worker "misc-archive" \
  "${COMMON_ARGS[@]}" \
  --exclude='Research Master/' \
  --exclude='Computer Backups/' \
  --include='/2022 GSI and NSI mailboxes/***' \
  --include='/External HDs/***' \
  --include='/Gunstruction/***' \
  --include='/Media/***' \
  --exclude='*' \
  "$SRC_ROOT/" \
  "$DEST_ROOT/"

echo ""
echo "Workers launched."
echo "Use 'tail -f $LOG_DIR/${timestamp}-<worker>.stdout' to monitor a worker."

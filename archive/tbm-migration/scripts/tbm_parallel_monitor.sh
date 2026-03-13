#!/bin/zsh

set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"

DEST_ROOT="${DEST_ROOT:-/Volumes/tbm_archive}"
INTERVAL="${INTERVAL:-300}"
LOG_DIR="${LOG_DIR:-$HOME/tbm-parallel-logs}"
AWK_BIN="${AWK_BIN:-$(command -v awk || true)}"
PERL_BIN="${PERL_BIN:-$(command -v perl || true)}"

latest_stdout_file() {
  local worker="$1"
  local latest

  latest="$(ls -1t "$LOG_DIR"/*-"$worker".stdout 2>/dev/null | head -n 1 || true)"
  echo "$latest"
}

latest_xfr_count() {
  local stdout_file="$1"

  if [[ -z "$stdout_file" || ! -f "$stdout_file" ]]; then
    echo "n/a"
    return
  fi

  local value
  value="$("$PERL_BIN" -ne 'while (/xfr#([0-9]+)/g) { $last = $1 } END { print defined($last) ? $last : "n/a" }' "$stdout_file" 2>/dev/null)"
  echo "${value:-n/a}"
}

latest_progress_bytes() {
  local stdout_file="$1"

  if [[ -z "$stdout_file" || ! -f "$stdout_file" ]]; then
    echo "0"
    return
  fi

  "$PERL_BIN" -e '
    use strict;
    use warnings;
    local $/ = undef;
    my $file = shift @ARGV;
    open my $fh, "<", $file or do { print "0"; exit 0; };
    my $text = <$fh>;
    my %mult = (
      "" => 1,
      K  => 1024,
      M  => 1024**2,
      G  => 1024**3,
      T  => 1024**4,
      P  => 1024**5,
    );
    my $last = 0;
    while ($text =~ /([0-9]+(?:\.[0-9]+)?)\s*([KMGTP]?)\s+\d+%\s+/g) {
      my ($num, $unit) = ($1, $2);
      $last = int($num * $mult{$unit});
    }
    print $last;
  ' "$stdout_file" 2>/dev/null
}

print_line() {
  local label="$1"
  local delta_bytes="$2"
  local delta_t="$3"

  "$AWK_BIN" -v label="$label" -v dbytes="$delta_bytes" -v dt="$delta_t" '
    BEGIN {
      mibs = (dt > 0) ? (dbytes / 1024.0 / 1024.0 / dt) : 0;
      moved = dbytes / 1024.0 / 1024.0;
      printf "%-14s %8.2f MiB moved  avg %7.2f MiB/s\n", label, moved, mibs;
    }
  '
}

if [[ ! -d "$DEST_ROOT" ]]; then
  echo "Destination root not found: $DEST_ROOT" >&2
  exit 1
fi

if [[ ! -d "$LOG_DIR" ]]; then
  echo "Log directory not found: $LOG_DIR" >&2
  exit 1
fi

if [[ -z "$AWK_BIN" || ! -x "$AWK_BIN" ]]; then
  echo "awk not found; set AWK_BIN explicitly" >&2
  exit 1
fi

if [[ -z "$PERL_BIN" || ! -x "$PERL_BIN" ]]; then
  echo "perl not found; set PERL_BIN explicitly" >&2
  exit 1
fi

echo "Monitoring ThunderBay parallel copy destinations"
echo "  interval:    ${INTERVAL}s"
echo "  logs:        $LOG_DIR"
echo ""

photos_stdout="$(latest_stdout_file "photos")"
nspace_stdout="$(latest_stdout_file "n-space")"
misc_stdout="$(latest_stdout_file "misc-archive")"

prev_photos="$(latest_progress_bytes "$photos_stdout")"
prev_nspace="$(latest_progress_bytes "$nspace_stdout")"
prev_misc="$(latest_progress_bytes "$misc_stdout")"
prev_t="$(date +%s)"

while true; do
  sleep "$INTERVAL"

  cur_t="$(date +%s)"
  dt=$((cur_t - prev_t))

  photos_stdout="$(latest_stdout_file "photos")"
  nspace_stdout="$(latest_stdout_file "n-space")"
  misc_stdout="$(latest_stdout_file "misc-archive")"

  cur_photos="$(latest_progress_bytes "$photos_stdout")"
  cur_nspace="$(latest_progress_bytes "$nspace_stdout")"
  cur_misc="$(latest_progress_bytes "$misc_stdout")"

  delta_photos=$(( cur_photos >= prev_photos ? cur_photos - prev_photos : 0 ))
  delta_nspace=$(( cur_nspace >= prev_nspace ? cur_nspace - prev_nspace : 0 ))
  delta_misc=$(( cur_misc >= prev_misc ? cur_misc - prev_misc : 0 ))
  delta_total=$(( delta_photos + delta_nspace + delta_misc ))

  photos_xfr="$(latest_xfr_count "$photos_stdout")"
  nspace_xfr="$(latest_xfr_count "$nspace_stdout")"
  misc_xfr="$(latest_xfr_count "$misc_stdout")"

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] rolling average over ${dt}s"
  print_line "photos" "$delta_photos" "$dt"
  echo "  files xfr#: $photos_xfr"
  print_line "n-space" "$delta_nspace" "$dt"
  echo "  files xfr#: $nspace_xfr"
  print_line "misc-archive" "$delta_misc" "$dt"
  echo "  files xfr#: $misc_xfr"
  print_line "TOTAL" "$delta_total" "$dt"
  echo ""

  prev_photos="$cur_photos"
  prev_nspace="$cur_nspace"
  prev_misc="$cur_misc"
  prev_t="$cur_t"
done

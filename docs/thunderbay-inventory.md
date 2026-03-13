# ThunderBay Inventory

This note records a read-only inventory of the mounted ThunderBay archive at:

- `/Volumes/ThunderBay mini/Research Master`

The goal of this inventory was to confirm the surviving assumptions in the dissertation repo about the original video/XML storage layout and the Python processing path.

## Inventory Date

- 2026-03-12

## Top-Level Structure

Observed top-level directories:

- `_inbox/`
- `data/`
- `raw_videos/`

This matches the broad structure described in [_apps/38h-dataorg.qmd](/Volumes/Casa/dev/dissertation/_apps/38h-dataorg.qmd).

## `data/` Tree

Observed counts:

- participant directories: `64`
- XML files: `124`
- participant directories with `videos/`: `62`

Two of the `64` participant directories are skip placeholders rather than full participant records:

- `1002-SKIP`
- `1004-SKIP`

That leaves `62` real participant directories, each with:

- `images/`
- `videos/`
- exactly two XML files

Representative participant directory shape:

```text
1001-PWI-2023-02-10-1200
├── 1001-Forms.pdf
├── 1001-Script.pdf
├── Participant Intake Sheet, p1  2.pdf
├── images/
└── videos/
    ├── 1001-Learn.mp4
    ├── 1001-Learn.wfp
    ├── 1001-Learn.xml
    ├── 1001-Recall.mp4
    ├── 1001-Recall.wfp
    └── 1001-Recall.xml
```

Interpretation:

- the ThunderBay `data/` tree is the normalized participant-level archive
- each real participant record appears to preserve forms/script PDFs, images, finished phase videos, Kyno project files, and Kyno XML exports

## `raw_videos/` Tree

Observed counts:

- raw video files: `275`

Observed structure:

- one directory per real participant id
- one `_unused/` directory

Representative raw filename patterns:

- `1001-learn-hl.mp4`
- `1001-learn-side.MOV`
- `1001-recall-hl.mp4`
- `1001-recall-side.MOV`
- `1005-learn-hl-1.mp4`
- `1005-learn-hl-2.mp4`
- `1007-learn-side-1.MOV`
- `1007-learn-side-2.MOV`
- `1026-learn-hl-p1.mp4`
- `1026-learn-hl-p2.mp4`
- `1039-learn-hl-p1.mp4`
- `1039-learn-hl-p2.mp4`

Interpretation:

- `raw_videos/` preserves the original capture layer
- split recordings and variant suffixes (`-1`, `-2`, `-p1`, `-p2`) survive here
- the participant `data/.../videos/` trees appear to preserve a more normalized per-phase result (`Learn` / `Recall`) after processing/selection

## Comparison To Surviving Repo Assumptions

### Confirmed

The inventory confirms the main assumptions in:

- [parse_xml/process_data.py](/Volumes/Casa/dev/dissertation/parse_xml/process_data.py)
- [archive/parse_xml-legacy/generate_combined_reports.py](/Volumes/Casa/dev/dissertation/archive/parse_xml-legacy/generate_combined_reports.py)
- [_apps/38h-dataorg.qmd](/Volumes/Casa/dev/dissertation/_apps/38h-dataorg.qmd)

Specifically:

- the historical ThunderBay root path used by `process_data.py` is correct:
  - `XML_ROOT = "/Volumes/ThunderBay mini/Research Master/data/"`
- participant directory naming follows the expected pattern:
  - `{participant}-{treatment}-{date}-{time}`
- the participant-level `data/` tree really is the XML/video/forms root used by the Python workflow
- the archive really does distinguish:
  - a normalized participant-level `data/` tree
  - a separate `raw_videos/` capture archive

Current follow-on implication:

- the refactored active extraction path should prefer the UNAS-backed replica as its working external root
- the old ThunderBay path remains important as historical provenance evidence, not as the default working target

### Clarified

The inventory strengthens the interpretation of the original processing flow:

1. raw video captures were first preserved under `raw_videos/`
2. participant-level records were assembled under `data/`
3. the `data/.../videos/` subtrees held the finished per-phase videos plus Kyno `.wfp` and `.xml`
4. the Python utilities then traversed that normalized `data/` tree to build timing CSVs and participant reports

It also clarifies that the two skip directories should not be treated as failed/missing participant folders in later inventories.

## Current Provenance Value

This inventory does not make the raw-data pipeline fully reproducible, but it does improve confidence in the surviving repo documentation by confirming that:

- the external ThunderBay assumptions in the Python code are substantially correct
- the external `data/` tree and `raw_videos/` tree had distinct roles
- the surviving in-repo artifacts (`data/reports/`, `data/csv/i1_times_v2.csv`, and the Python utilities) still line up with the actual archive structure

## Migration To UNAS

After the inventory and path-validation work, the ThunderBay archive was copied to the UNAS Pro as a new primary working archive location.

Destination:

- UNAS Pro share: `tbm_archive`
- mounted copy target on macOS: `/Volumes/tbm_archive/research_master/`

Migration method:

- source mounted on macOS from the ThunderBay
- destination mounted on macOS over SMB from the UNAS Pro
- the Mac was moved onto the `Private` VLAN so both endpoints were on the `10.24.2.x` subnet
- the successful full copy used Homebrew `rsync 3.4.1` with `caffeinate`

Representative command form:

```bash
caffeinate -disu rsync -aHh --info=progress2 --partial --append-verify \
  --exclude='.DS_Store' \
  --exclude='.LP_Store/' \
  --exclude='._*' \
  --log-file="$HOME/tbm-to-unas-rsync.log" \
  "/Volumes/ThunderBay mini/Research Master/" \
  "/Volumes/tbm_archive/research_master/"
```

Notes:

- the system `rsync` on macOS was too old for `--info=progress2`; the actual successful transfer used the Homebrew `rsync`
- early SMB tests on the `Core` VLAN were much slower; moving the Mac to the `Private` VLAN materially improved throughput
- observed sustained throughput during the full copy was on the order of `~115 MB/s`, with transient rates near `200 MB/s`
- the ad hoc helper scripts used during that migration are now preserved at `archive/tbm-migration/scripts/` for historical reference only; they are not part of the active dissertation workflow

### Verification

The migration was verified with:

1. checkpoint counts against the earlier ThunderBay inventory
2. a permission-neutral `rsync --dry-run` from source to destination

Verified counts:

- `data/` participant directories: `64` on source and destination
- XML files under `data/`: `124` on source and destination
- `raw_videos/` file count after excluding macOS junk: `267` on source and destination

Verification command:

```bash
/opt/homebrew/bin/rsync -rltDhn --delete --itemize-changes \
  --exclude='.DS_Store' \
  --exclude='.LP_Store/' \
  --exclude='._*' \
  "/Volumes/ThunderBay mini/Research Master/" \
  "/Volumes/tbm_archive/research_master/"
```

Result:

- no content differences reported
- earlier comparison noise was limited to SMB permission differences, not missing files

Current interpretation:

- the UNAS copy is now a verified replica of the ThunderBay archive, modulo the intentionally excluded macOS junk
- the ThunderBay should be treated as the old physical source location until you explicitly decide its final disposition, but the UNAS path is now the primary working archive location

## Next Related Work

The next ThunderBay-focused tasks should be:

1. document the destination paths and migration mapping more fully in the homelab notes as needed
2. relate the participant-level archive more explicitly to:
   - `data/reports/`
   - `data/csv/i1_times_v2.csv`
   - `data/source/notes/`
3. decide whether a few key non-video precursor files should be staged inside the repo tree for backup convenience while remaining out of git
4. decide the final disposition of the physical ThunderBay after the verified UNAS migration

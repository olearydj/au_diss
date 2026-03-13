# ThunderBay Migration Archive

This folder preserves a small amount of operational residue from the completed ThunderBay -> UNAS archive migration.

These files are not part of the active dissertation workflow, manuscript build, or data-curation pipeline. They are retained only as historical reference because the verified UNAS copy now forms part of the provenance context documented in `docs/thunderbay-inventory.md`.

## Contents

### `scripts/tbm_parallel_copy.sh`

- Status: archived helper script
- Role:
  - launches a parallelized `rsync`-based copy workflow used during the broader ThunderBay -> UNAS migration work
- Use boundary:
  - not a maintained dissertation utility
  - preserved only to show one of the operational approaches used during the completed migration

### `scripts/tbm_parallel_monitor.sh`

- Status: archived helper script
- Role:
  - monitors the rolling transfer progress of the parallel copy workers above by parsing their stdout logs
- Use boundary:
  - not a maintained dissertation utility
  - preserved only as supporting operational context for the prior migration effort

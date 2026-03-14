# Local Snapshots

This directory is a local convenience view of preserved dissertation output bundles.

It is intentionally separate from the tracked archival/release structure:

- [`../defended-2024-08-02/`](/Volumes/Casa/dev/dissertation/defended-2024-08-02) remains the public, tracked defended snapshot
- `verified-2026-03-14/` is a local preserved copy of the modern verified rebuild outputs

Expected local layout:

```text
snapshots/
  README.md
  defended-2024-08-02 -> ../defended-2024-08-02
  verified-2026-03-14/
    README.md
    dissertation.pdf
    html/
```

The `defended-2024-08-02` entry is a symlink back to the tracked archival folder so the canonical defended materials stay in their established public location.

The `verified-2026-03-14` snapshot is a local copy of the rebuild outputs associated with:

- tag: `rebuild/dissertation-arm64-verified-2026-03-14`
- release: `Modern Arm64 Rebuild Snapshot (2026-03-14)`

Snapshot contents are ignored by git so they can be refreshed, removed, or replaced without affecting repository history.

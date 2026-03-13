# parse_xml

This directory holds the upstream XML extraction layer for the dissertation data pipeline.

## Recommended Entry Point

Use [`process_data.py`](/Volumes/Casa/dev/dissertation/parse_xml/process_data.py) as the active script.

It reads:

- `data/source/i1_raw_data.xlsx`
- `data/source/notes/*.md`
- participant XML exports from the external archive root

It writes:

- `data/reports/*-combined.md`
- `data/csv/i1_times_v2.csv`

## Path Configuration

`process_data.py` now supports additive path configuration through CLI options or environment variables:

- data root:
  `--data-root` or `DISS_DATA_ROOT`
- external participant/XML archive root:
  `--xml-root` or `DISS_XML_ROOT`
- optional Box/video link root for markdown report links:
  `--box-root` or `DISS_BOX_ROOT`

Default behavior:

- `data/` defaults to the current repository `data/` tree
- XML root prefers the UNAS-backed archive at `/Volumes/tbm_archive/research_master/data` and falls back to the legacy ThunderBay path if needed
- markdown report links preserve the historical Box Sync root unless you override it

## Recommended Current Invocation

```bash
uv run python parse_xml/process_data.py \
  --xml-root /Volumes/tbm_archive/research_master/data
```

The root [`pyproject.toml`](/Volumes/Casa/dev/dissertation/pyproject.toml) is now the active Python environment entry point for this workflow.
The legacy [`requirements.txt`](/Volumes/Casa/dev/dissertation/requirements.txt) is retained as historical reference.

## Legacy Scripts

- `generate_combined_reports.py`: older wrapper retained as historical reference
- `process_video_tree.py`: earliest wrapper attempt retained as historical reference
- `parse_xml.py`: lower-level XML parser/report helper still used by the legacy wrapper path

These are intentionally preserved, but `process_data.py` is the script that should be treated as the clean switch-over target.

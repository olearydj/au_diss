# parse_xml-legacy

This directory preserves earlier inactive generations of the dissertation XML/report-processing workflow.

These files are not the active extraction path. They are retained because they document the development history that preceded the surviving `process_data.py` generation.

## Generation Order

1. `process_video_tree.py`
   - earliest wrapper attempt
   - walks an XML tree and writes markdown reports
2. `generate_combined_reports.py`
   - second-generation wrapper
   - combines handwritten notes with XML-derived report content and an earlier timing CSV path
3. `parse_xml.py`
   - low-level XML parser/report helper used by the older wrappers
4. `test_input/` and `test_output/`
   - sample XML fixtures and generated markdown outputs used with the archived low-level parser
5. `requirements.txt`
   - legacy Python environment specification retained as a historical reference alongside the older scripts
6. `parse_xml.code-workspace`
   - local workspace artifact kept only as part of the historical package

## Active Replacement

The active extraction entry point is now [`parse_xml/process_data.py`](/Volumes/Casa/pub/dissertation/parse_xml/process_data.py), supported by [`parse_xml/path_config.py`](/Volumes/Casa/pub/dissertation/parse_xml/path_config.py) and the root [`pyproject.toml`](/Volumes/Casa/pub/dissertation/pyproject.toml).

Recommended current invocation:

```bash
uv run python parse_xml/process_data.py \
  --xml-root /Volumes/tbm_archive/research_master/data
```

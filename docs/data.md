# Data Tree And Generation Flow

This note records the current understanding of the dissertation data tree, the source-to-curated workflow, and the boundary between what is preserved in the repository and what lived on external storage.

## Overview

The repository preserves multiple layers of research data:

- source spreadsheets used for curation and manual correction
- participant note markdown
- generated participant reports
- intermediate timing CSVs
- curated analysis workbooks
- saved R objects used directly by the manuscript build
- a separate retention/H3 support workbook added later

These layers should not be treated as duplicates. They represent different stages of the original workflow.

## In-Repo Versus External Data

### Preserved In Repo

- `data/DataDictionary.docx`
- `data/source/i1_raw_data.xlsx`
- `data/source/adjusted_drop_events.xlsx`
- `data/source/i1_h3.xlsx`
- `data/source/notes/`
- `data/reports/`
- `data/csv/i1_times_v1.csv`
- `data/csv/i1_times_v2.csv`
- `data/combined_results.xlsx`
- `rdata/`
- `parse_xml/test_input/` and `parse_xml/test_output/`

One additional documentation artifact also survives in the data tree:

- `data/DataDictionary.docx`

Current interpretation:

- this is an auxiliary documentation artifact associated with the unfinished appendix stub in [_apps/37g-datadict.qmd](/Volumes/Casa/dev/dissertation/_apps/37g-datadict.qmd)
- it is not part of the active manuscript build
- it is worth preserving in its historical location until a later markdown conversion/cleanup pass

### External / Machine-Specific Roots

The original raw video and XML workflow depended on external paths that are not preserved in the repo itself:

- ThunderBay RAID / external storage:
  - `/Volumes/ThunderBay mini/Research Master/data/`
  - `/Volumes/ThunderBay mini/Research Master/raw_videos/`
- Box Sync mirror used for local/cloud access to participant trial-data:
  - `/Users/djo/Box Sync/Tiger Motors Research Team Collaboration Files/Investigation 1 Data Files/trial-data/`

These locations are described in [_apps/38h-dataorg.qmd](/Volumes/Casa/dev/dissertation/_apps/38h-dataorg.qmd) and hard-coded in the Python utilities under [`parse_xml/`](/Volumes/Casa/dev/dissertation/parse_xml).

Practical implication:

- the current manuscript rebuild does **not** require those external roots
- a full raw-to-curated regeneration of the timing/report layer **does** depend on them

## Main Phase 1 / Phase 2 Data Path

The main study workflow appears to have been:

1. Raw participant/session information entered into `data/source/i1_raw_data.xlsx`
2. Participant observation notes and feedback maintained in `data/source/notes/`
3. Kyno XML exports produced from annotated videos stored externally under the ThunderBay `data/` tree
4. Python processing used those notes, XML files, and workbook data to generate:
   - participant reports in `data/reports/`
   - timing CSV output in `data/csv/i1_times_v2.csv`
5. `forms_data.Rmd` read:
   - workbook tabs from `data/source/i1_raw_data.xlsx`
   - timing data from `data/csv/i1_times_v2.csv`
   - manual event corrections from `data/source/adjusted_drop_events.xlsx`
6. `forms_data.Rmd` produced:
   - QA/debug CSVs in `test/`
   - curated workbook `data/combined_results.xlsx`
7. The manuscript Results workflow read `data/combined_results.xlsx` plus supporting `rdata/*.RData`

## Python Processing Layer

The Python files in [`parse_xml/`](/Volumes/Casa/dev/dissertation/parse_xml) represent successive generations of the annotation/report workflow.

### `parse_xml/parse_xml.py`

- low-level XML parser and markdown report generator
- reads a Kyno XML export
- extracts metadata, subclip markers, and other markers
- builds markdown-ready report sections
- includes a simple local test harness using `parse_xml/test_input/` and `parse_xml/test_output/`

### `parse_xml/process_video_tree.py`

- earliest wrapper attempt
- walks an XML tree and writes markdown reports
- uses hard-coded dev/prod/output roots

### `parse_xml/generate_combined_reports.py`

- second-generation wrapper
- combines hand-transcribed markdown notes with XML-derived report content
- writes combined reports and an earlier timing CSV
- still uses hard-coded dissertation/dev and ThunderBay roots

### `parse_xml/process_data.py`

- most complete surviving generation of the Python workflow
- reads:
  - `data/source/notes/`
  - `data/source/i1_raw_data.xlsx`
  - XML files from the external ThunderBay tree
- writes:
  - `data/reports/*-combined.md`
  - `data/csv/i1_times_v2.csv`
- still contains hard-coded local paths:
  - `DATA_ROOT = "/Users/djo/dev/au/dissertation/data/"`
  - `XML_ROOT = "/Volumes/ThunderBay mini/Research Master/data/"`
  - `BOX_ROOT = "/Users/djo/Box%20Sync/.../trial-data/"`

Current interpretation:

- `process_data.py` is the clearest surviving source for how `data/reports/` and `data/csv/i1_times_v2.csv` were generated
- it is not currently portable without path refactoring

## R Curation Layer

[`forms_data.Rmd`](/Volumes/Casa/dev/dissertation/forms_data.Rmd) is the key R-side data curation notebook.

It reads:

- demographics, outcomes, TLX, SUS, and BCS sheets from `data/source/i1_raw_data.xlsx`
- timing/event data from `data/csv/i1_times_v2.csv`
- manual adjustment data from `data/source/adjusted_drop_events.xlsx`

It then:

- cleans demographics and outcomes
- classifies/patches event timing data
- joins timing and outcome information
- computes aggregated event summaries
- produces TLX and SUS score tables
- exports QA/debug CSVs into `test/`
- exports the curated workbook `data/combined_results.xlsx`

Important historical note:

- `forms_data.Rmd` still contains a TODO to `add phase 3`
- this confirms that the main curated workbook path stopped at phases 1 and 2

## Meaning Of `test/`

The ignored top-level `test/` directory is not unit tests. It is a set of QA/debug outputs written by `forms_data.Rmd`, including:

- `test/outcomes.csv`
- `test/times.csv`
- `test/joined.csv`
- `test/joined_aug.csv`
- `test/combined.csv`
- `test/tlx_scores.csv`

These are intermediate inspection dumps used to validate the curation pipeline. They are useful for forensic understanding, but they are not manuscript inputs.

## Meaning Of `parse_xml/test_input/` And `parse_xml/test_output/`

These directories are a small parser test harness:

- `parse_xml/test_input/`: sample XML files
- `parse_xml/test_output/`: expected/generated markdown reports from those samples

They are useful for understanding and testing `parse_xml.py`, but they are not part of the dissertation manuscript build.

Current recommendation:

- keep this fixture harness fully tracked and internally consistent
- include the local `1001-Learn.xml` sample that had previously been ignored only because of a broad `test_input/` ignore rule

## Retention / H3 Data Path

Retention/H3 was handled differently from the main phase 1 / phase 2 workflow.

- `forms_data.Rmd` exports `data/combined_results.xlsx` but still carries a TODO to "add phase 3"
- the retention analysis instead reads `data/source/i1_h3.xlsx` directly
- H3 then joins that sheet with:
  - `demographics` from `data/combined_results.xlsx`
  - recall-derived objects from `rdata/`

Current interpretation, supported by author confirmation:

- H3 analysis was deferred
- it was later completed more ad hoc
- the retention data was never folded back into the original aggregated workbook pipeline

So `data/source/i1_h3.xlsx` should be treated as a legitimate retained source artifact for the retention analysis, not as an orphaned duplicate.

## Saved R Objects

`rdata/` contains saved objects used directly by the manuscript build, including:

- derived datasets such as `learn`, `recall`, and `res_f`
- shared helper functions/themes in `shared.RData`
- saved bootstrap outputs
- saved robust-model fits for H1b/H2 sections

These files are part of the current render path and should be treated as baseline-support artifacts rather than disposable cache.

## Reproducibility Boundary

For current baselining purposes:

- the manuscript build is reproducible from the preserved curated artifacts in the repo
- the full raw-to-curated processing path is only partly reproducible because it depends on:
  - external video/XML roots
  - manual note entry and manual event adjustments
  - historically local storage conventions

So the repo baseline should document the full path honestly, rather than pretending it is a fully self-contained raw-data pipeline.

## Current Baseline Interpretation

For current baselining purposes:

- keep the full `data/` tree
- treat `data/source/` as source/curation inputs
- treat `data/reports/` as generated but historically meaningful support artifacts
- treat `data/csv/i1_times_v2.csv` as the surviving Python-to-R handoff artifact for the main timing path
- treat `data/combined_results.xlsx` as the canonical curated workbook for the main study
- treat `data/source/i1_h3.xlsx` as the separate but legitimate H3 retention source workbook

## Remaining Documentation Gaps

The biggest remaining documentation gaps are:

1. the exact original sequence used to produce `data/csv/i1_times_v2.csv` from the external XML tree
2. whether `data/reports/` should be treated as primary generated outputs or as an intermediate reporting/debug layer
3. whether `data/reports/` should be treated as primary generated outputs or as an intermediate reporting/debug layer
4. whether the `test/` QA CSVs should remain purely ignored local residue or be archived elsewhere as pipeline evidence
5. whether `data/DataDictionary.docx` should later be converted into a markdown/native repo document and folded into the appendix/docs structure

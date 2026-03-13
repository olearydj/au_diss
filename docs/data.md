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
- `archive/parse_xml-legacy/`

Current interpretation:

- this is an auxiliary documentation artifact associated with the unfinished appendix stub in [_apps/37g-datadict.qmd](/Volumes/Casa/dev/dissertation/_apps/37g-datadict.qmd)
- it is not part of the active manuscript build
- it is worth preserving in its historical location until a later markdown conversion/cleanup pass

### External / Machine-Specific Roots

The original raw video and XML workflow depended on external paths that are not preserved in the repo itself:

- Original ThunderBay source/archive:
  - `/Volumes/ThunderBay mini/Research Master/data/`
  - `/Volumes/ThunderBay mini/Research Master/raw_videos/`
- Current UNAS replica/archive:
  - `/Volumes/tbm_archive/research_master/`
- Box Sync mirror used for local/cloud access to participant trial-data:
  - `/Users/djo/Box Sync/Tiger Motors Research Team Collaboration Files/Investigation 1 Data Files/trial-data/`

These locations are described in [_apps/38h-dataorg.qmd](/Volumes/Casa/dev/dissertation/_apps/38h-dataorg.qmd).

Historically, the Python extraction utilities under [`parse_xml/`](/Volumes/Casa/dev/dissertation/parse_xml) hard-coded these paths. The active extraction entry point now supports path overrides via CLI options or environment variables, while preserving the historical path assumptions as documented context.

A read-only inventory of the surviving ThunderBay archive was completed on 2026-03-12 and is recorded in [thunderbay-inventory.md](/Volumes/Casa/dev/dissertation/docs/thunderbay-inventory.md).

That note now also records the subsequent migration of the archive onto the UNAS Pro and the verification steps used to confirm the copy.

Practical implication:

- the current manuscript rebuild does **not** require those external roots
- a full raw-to-curated regeneration of the timing/report layer **does** depend on them

Important clarification from the ThunderBay inventory:

- the external `data/` tree is the normalized participant-level archive
- the external `raw_videos/` tree is the original capture/archive layer
- the Python processing path appears to have traversed the normalized participant-level `data/` tree rather than the raw capture archive
- the UNAS copy is now a verified replica of the ThunderBay archive and should be treated as the primary working external archive path

## Main Phase 1 / Phase 2 Data Path

The main study workflow appears to have been:

1. Raw participant/session information entered into `data/source/i1_raw_data.xlsx`
2. Participant observation notes and feedback maintained in `data/source/notes/`
3. Kyno XML exports produced from annotated videos stored externally under the ThunderBay `data/` tree
4. Python processing used those notes, XML files, and workbook data to generate:
   - participant reports in `data/reports/`
   - timing CSV output in `data/csv/i1_times_v2.csv`
5. `analysis/forms_data/forms_data.Rmd` read:
   - workbook tabs from `data/source/i1_raw_data.xlsx`
   - timing data from `data/csv/i1_times_v2.csv`
   - manual event corrections from `data/source/adjusted_drop_events.xlsx`
6. `analysis/forms_data/forms_data.Rmd` produced:
   - QA/debug CSVs in `analysis/forms_data/output/`
   - curated workbook `data/combined_results.xlsx`
7. The manuscript Results workflow read `data/combined_results.xlsx` plus supporting `rdata/*.RData`

The 2026-03-12 ThunderBay inventory supports this interpretation more concretely:

- `data/` on ThunderBay contains `64` participant directories, of which `62` are real participant records and `2` are skip placeholders
- the `62` real participant directories each contain `images/`, `videos/`, and exactly two XML files
- `raw_videos/` separately preserves the raw camera/HoloLens capture layer, including split recordings such as `-1`, `-2`, `-p1`, and `-p2`

## Python Processing Layer

The active extraction entry point now lives in [`parse_xml/`](/Volumes/Casa/dev/dissertation/parse_xml), while earlier false starts are preserved under [`archive/parse_xml-legacy/`](/Volumes/Casa/dev/dissertation/archive/parse_xml-legacy).

### `parse_xml/process_data.py`

- most complete surviving generation of the Python workflow
- reads:
  - `data/source/notes/`
  - `data/source/i1_raw_data.xlsx`
  - XML files from the external ThunderBay tree
- writes:
  - `data/reports/*-combined.md`
  - `data/csv/i1_times_v2.csv`
- now supports additive path configuration for:
  - repo `data/` root
  - external participant/XML archive root
  - optional Box/video-link root used in generated markdown reports
- current defaults:
  - repo `data/` root resolves to the current repository `data/` tree
  - XML root prefers `/Volumes/tbm_archive/research_master/data/` and falls back to the legacy ThunderBay path if needed
  - markdown report links preserve the historical Box Sync root unless explicitly overridden

### `parse_xml/path_config.py`

- path/config helper used by the active extraction entry point
- centralizes the repo `data/` root, external XML root, and optional Box link root resolution
- prefers the verified UNAS archive as the default working external root while retaining the legacy ThunderBay path as fallback/provenance context

### `archive/parse_xml-legacy/process_video_tree.py`

- earliest wrapper attempt
- walks an XML tree and writes markdown reports
- uses hard-coded dev/prod/output roots

### `archive/parse_xml-legacy/generate_combined_reports.py`

- second-generation wrapper
- combines hand-transcribed markdown notes with XML-derived report content
- writes combined reports and an earlier timing CSV
- still uses hard-coded dissertation/dev and ThunderBay roots

### `archive/parse_xml-legacy/parse_xml.py`

- low-level XML parser and markdown report generator used by the archived wrappers
- reads a Kyno XML export
- extracts metadata, subclip markers, and other markers
- builds markdown-ready report sections
- uses the archived sample fixture harness under `archive/parse_xml-legacy/test_input/` and `archive/parse_xml-legacy/test_output/`

Current interpretation:

- `process_data.py` is the clearest surviving source for how `data/reports/` and `data/csv/i1_times_v2.csv` were generated
- it is now the clean switch-over target for a configurable extraction path
- its assumptions about the ThunderBay path and participant directory naming were confirmed by the 2026-03-12 inventory
- the recommended current working external archive root is the verified UNAS copy, not the physical ThunderBay

## R Curation Layer

[`analysis/forms_data/forms_data.Rmd`](/Volumes/Casa/dev/dissertation/analysis/forms_data/forms_data.Rmd) is the key R-side data curation notebook.

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
- exports QA/debug CSVs into `analysis/forms_data/output/`
- exports the curated workbook `data/combined_results.xlsx`

Important historical note:

- `analysis/forms_data/forms_data.Rmd` still contains a TODO to `add phase 3`
- this confirms that the main curated workbook path stopped at phases 1 and 2

## Meaning Of `analysis/forms_data/output/`

The ignored `analysis/forms_data/output/` directory is not unit tests. It is a set of QA/debug outputs written by `analysis/forms_data/forms_data.Rmd`, including:

- `analysis/forms_data/output/outcomes.csv`
- `analysis/forms_data/output/times.csv`
- `analysis/forms_data/output/joined.csv`
- `analysis/forms_data/output/joined_aug.csv`
- `analysis/forms_data/output/combined.csv`
- `analysis/forms_data/output/tlx_scores.csv`

These are intermediate inspection dumps used to validate the curation pipeline. They are useful for forensic understanding, but they are not manuscript inputs.

## Meaning Of `archive/parse_xml-legacy/test_input/` And `archive/parse_xml-legacy/test_output/`

These directories are a small parser test harness:

- `archive/parse_xml-legacy/test_input/`: sample XML files
- `archive/parse_xml-legacy/test_output/`: expected/generated markdown reports from those samples

They are useful for understanding and testing the archived low-level parser, but they are not part of the dissertation manuscript build.

Current recommendation:

- keep this fixture harness fully tracked as archival support material
- keep it adjacent to the archived legacy parser generations rather than the active extraction entry point

## Retention / H3 Data Path

Retention/H3 was handled differently from the main phase 1 / phase 2 workflow.

- `analysis/forms_data/forms_data.Rmd` exports `data/combined_results.xlsx` but still carries a TODO to "add phase 3"
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

## Refactor Direction

The current repository now distinguishes two different executable layers that should not be conflated.

- `parse_xml/` is the upstream extraction layer:
  it depends on the external participant/XML archive and produces `data/reports/` plus `data/csv/i1_times_v2.csv`
- `archive/parse_xml-legacy/` preserves the earlier false starts and parser fixtures that preceded the active entry point
- `analysis/forms_data/` is the R-side curation layer:
  it consumes the preserved workbook and timing artifacts and produces local QA outputs plus `data/combined_results.xlsx`

Current recommendation:

1. keep `analysis/forms_data/` as the home of the active R curation notebook and its local QA output folder
2. keep `parse_xml/` separate for now, because it is an external-archive extraction layer rather than manuscript analysis
3. if a broader cleanup is worth doing later, consider a higher-level `pipeline/` grouping rather than folding the Python extractor directly into `analysis/`
4. if that later refactor happens, the first Python cleanup should be path/config normalization so the UNAS-backed archive becomes the documented primary working external root

## Validation Rule For Extraction Refactors

For the Python extraction layer, structural cleanup is not enough by itself.

Any path/config refactor should be treated as incomplete until the refactored entry point can generate hash-matching outputs for:

- `data/csv/i1_times_v2.csv`
- `data/reports/*-combined.md`

using a disposable output location and the preserved dissertation inputs.

## Remaining Documentation Gaps

The biggest remaining documentation gaps are:

1. the exact original sequence used to produce `data/csv/i1_times_v2.csv` from the external XML tree
2. whether `data/reports/` should be treated as primary generated outputs or as an intermediate reporting/debug layer
3. whether the `analysis/forms_data/output/` QA CSVs should remain purely ignored local residue or be archived elsewhere as pipeline evidence
4. whether `data/DataDictionary.docx` should later be converted into a markdown/native repo document and folded into the appendix/docs structure

The ThunderBay inventory closed some uncertainty about the external archive structure, but it did not yet reconstruct the exact transformation sequence from:

- `raw_videos/`
- ThunderBay participant `data/.../videos/*.xml`
- `data/source/notes/`

to:

- `data/reports/`
- `data/csv/i1_times_v2.csv`

The archive-migration work also leaves one practical documentation task:

- update any remaining external-path notes and future workflow docs so they refer to the UNAS-backed archive as the primary working location rather than the physical ThunderBay

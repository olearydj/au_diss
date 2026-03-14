# End-to-End Research Pipeline

This note is the canonical overview of the dissertation's documented research pipeline.

It is written for technically capable researchers who want to understand what each stage did, why it existed, what artifacts are preserved, and how much of the workflow can reasonably be reproduced today.

## What This Pipeline Produces

For the main phase 1 / phase 2 study, the documented pipeline turns a mix of manually maintained source materials and externally stored video-annotation exports into:

- participant-level generated reports in [`data/reports/`](/Volumes/Casa/dev/dissertation/data/reports), markdown format
- a timing/event handoff file in [`data/csv/i1_times_v2.csv`](/Volumes/Casa/dev/dissertation/data/csv/i1_times_v2.csv)
- a curated analysis workbook in [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx)
- manuscript analysis inputs, primarily [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx) plus saved objects under [`rdata/`](/Volumes/Casa/dev/dissertation/rdata), used by the Quarto dissertation build

In compact form, the main path is:

```text
external participant/XML archive
  + data/source/i1_raw_data.xlsx
  + data/source/notes/
    -> parse_xml/process_data.py
      -> data/reports/
      -> data/csv/i1_times_v2.csv
        -> analysis/forms_data/forms_data.Rmd
          -> analysis/forms_data/output/
          -> data/combined_results.xlsx
            -> manuscript analysis + rdata/*.RData
              -> Quarto PDF / HTML build
```

Retention/H3 is a partial exception to that path:

- the main workbook-generation flow stops at phases 1 and 2
- the later H3 analysis reads [`data/source/i1_h3.xlsx`](/Volumes/Casa/dev/dissertation/data/source/i1_h3.xlsx) separately
- H3 then joins that workbook with demographics from [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx) and recall-derived objects from [`rdata/`](/Volumes/Casa/dev/dissertation/rdata)

## Key Preserved Materials

The most important preserved artifacts are:

- [`data/source/i1_raw_data.xlsx`](/Volumes/Casa/dev/dissertation/data/source/i1_raw_data.xlsx): the main hand-generated source workbook holding participant/session metadata, outcomes, and questionnaire sheets that feed both the Python extraction step and the later R curation step; XLSX was preferred for numerical data-entry tasks.
- [`data/source/notes/`](/Volumes/Casa/dev/dissertation/data/source/notes): participant-level markdown notes preserving observational comments and feedback used in generated participant reports; markdown was preferred for qualitative feedback.
- [`data/source/adjusted_drop_events.xlsx`](/Volumes/Casa/dev/dissertation/data/source/adjusted_drop_events.xlsx): manually collected correction material used by the R curation notebook to patch drop-related timing cases where the system lost tracking and times needed adjustment.
- [`data/reports/`](/Volumes/Casa/dev/dissertation/data/reports): generated participant reports combining workbook information, notes, and XML-derived metadata into human-readable summaries meant to provide a single per-participant reference.
- [`data/csv/i1_times_v2.csv`](/Volumes/Casa/dev/dissertation/data/csv/i1_times_v2.csv): the Python-to-R handoff file for event timing data, generated from XML-derived timing/event information; it is not just an export of the original workbook, and the later manual drop-time adjustments are applied in R rather than here.
- [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx): the authoritative curated main-study workbook for phases 1 and 2, produced by [`analysis/forms_data/forms_data.Rmd`](/Volumes/Casa/dev/dissertation/analysis/forms_data/forms_data.Rmd) from the source workbook, the Python timing handoff file, and the manual drop-adjustment workbook.
- [`rdata/`](/Volumes/Casa/dev/dissertation/rdata): saved R objects used directly by the dissertation analyses and manuscript render path.
- [`archive/parse_xml-legacy/`](/Volumes/Casa/dev/dissertation/archive/parse_xml-legacy): earlier Python false starts and fixtures retained for provenance, but no longer the active extraction path.

The main missing boundary is the external participant XML/video archive.

Historically it lived on ThunderBay:

- `/Volumes/ThunderBay mini/Research Master/data/`
- `/Volumes/ThunderBay mini/Research Master/raw_videos/`

The verified active working replica is now on the UNAS:

- `/Volumes/tbm_archive/research_master/`

Current interpretation:

- the UNAS-backed archive is the active external source that the documented extraction workflow should use
- the old ThunderBay paths remain historical provenance evidence only

The external archive structure and the ThunderBay -> UNAS relationship are documented in [thunderbay-inventory.md](/Volumes/Casa/dev/dissertation/docs/thunderbay-inventory.md).

## How The Toolchains Map To The Workflow

The repo now has four distinct executable layers:

- Python: extracts participant timing and generated report artifacts from the external XML archive plus in-repo source materials.
- R curation: transforms extracted timing and source workbook materials into the curated main-study workbook.
- R analysis: works from the curated workbook and related derived objects to prepare analysis objects used in the manuscript.
- Quarto + Pandoc + LaTeX: renders the dissertation manuscript and HTML output from the curated data and manuscript-side analysis objects.

That separation matters because each layer has a different reproducibility status and a different relationship to the canonical defended artifacts.

## Recover Participant Timing And Reports With Python

The active extraction entry point is [`parse_xml/process_data.py`](/Volumes/Casa/dev/dissertation/parse_xml/process_data.py), with environment metadata in [`pyproject.toml`](/Volumes/Casa/dev/dissertation/pyproject.toml).

What this stage reads:

- [`data/source/i1_raw_data.xlsx`](/Volumes/Casa/dev/dissertation/data/source/i1_raw_data.xlsx): participant/session information and workbook tabs that help contextualize the extracted data.
- [`data/source/notes/`](/Volumes/Casa/dev/dissertation/data/source/notes): hand-transcribed notes and participant feedback.
- XML files under the external participant archive: Kyno annotation exports associated with per-participant video records.

What this stage produces:

- [`data/reports/`](/Volumes/Casa/dev/dissertation/data/reports): participant-level generated markdown reports tying together notes, workbook details, and XML/video metadata
- [`data/csv/i1_times_v2.csv`](/Volumes/Casa/dev/dissertation/data/csv/i1_times_v2.csv): event timing rows later consumed by the R curation notebook

How to run it today:

```bash
uv run python parse_xml/process_data.py \
  --xml-root /Volumes/tbm_archive/research_master/data
```

The script also supports additive path overrides through `--data-root`, `--xml-root`, `--box-root` or the corresponding `DISS_*` environment variables.

For validation work, it is safer to write into a disposable output tree instead of overwriting tracked dissertation artifacts.

Current reproducibility status:

- this is the clean active extraction path
- it has already been validated against the UNAS archive
- regenerated outputs were confirmed to hash-match the tracked [`data/reports/`](/Volumes/Casa/dev/dissertation/data/reports) files and [`data/csv/i1_times_v2.csv`](/Volumes/Casa/dev/dissertation/data/csv/i1_times_v2.csv)

## Curate The Analysis Workbook With R

The active curation entry point is [`analysis/forms_data/forms_data.Rmd`](/Volumes/Casa/dev/dissertation/analysis/forms_data/forms_data.Rmd).

This notebook is the documented middle layer of the dissertation data pipeline. Its role is to transform extracted timing data plus workbook/source corrections into the curated analysis workbook used by the manuscript.

What this stage reads:

- [`data/source/i1_raw_data.xlsx`](/Volumes/Casa/dev/dissertation/data/source/i1_raw_data.xlsx): demographics, outcomes, TLX, SUS, and related source sheets.
- [`data/csv/i1_times_v2.csv`](/Volumes/Casa/dev/dissertation/data/csv/i1_times_v2.csv): event timing output from the Python extraction stage.
- [`data/source/adjusted_drop_events.xlsx`](/Volumes/Casa/dev/dissertation/data/source/adjusted_drop_events.xlsx): manual corrections for drop-event timing adjustments.

What this stage does:

- cleans demographics and outcomes from the source workbook
- classifies and patches event timing rows from `i1_times_v2.csv`
- joins timing, outcomes, and manual corrections
- computes aggregated child-event counts and durations, for example rolling multiple child `pwi` events associated with a single car into per-car count and duration fields in the curated workbook
- produces TLX and SUS score tables
- writes the curated main-study workbook used by the manuscript analysis

What this stage produces:

- [`analysis/forms_data/output/`](/Volumes/Casa/dev/dissertation/analysis/forms_data/output): local QA/debug CSVs used to inspect intermediate curation results.
- [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx): the authoritative curated main-study workbook for phases 1 and 2.

How to run it today from an R session:

```r
.libPaths(c(
  "/Volumes/Casa/dev/dissertation/renv/library/macos/R-4.4/aarch64-apple-darwin20",
  .libPaths()
))
rmarkdown::render("analysis/forms_data/forms_data.Rmd")
```

Current reproducibility status:

- the notebook remains the best documented record of the workbook-generation logic
- the preserved workbook and QA outputs remain authoritative artifacts
- the notebook now reruns successfully under the current arm64 R environment after replacing one strict floating-point equality assertion with a tolerance-based check
- the generated QA/debug CSVs hash-match the preserved repo outputs exactly
- the regenerated workbook reads back identically through `readxl`, but the exact XLSX file hash can still drift because the spreadsheet container/writer layer is not byte-stable across rebuilds

So this stage is now practically reproducible for logical contents, even though exact byte-for-byte reproduction of [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx) remains sensitive to XLSX serialization details.

## Build The Manuscript From Curated Artifacts

The manuscript analysis/build boundary starts after [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx) and [`rdata/`](/Volumes/Casa/dev/dissertation/rdata).

What this stage reads:

- [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx): the curated main-study workbook.
- saved objects under [`rdata/`](/Volumes/Casa/dev/dissertation/rdata): derived datasets, helper objects, and model results used directly by the manuscript analyses.
- Quarto source under [`_front/`](/Volumes/Casa/dev/dissertation/_front), [`_chaps/`](/Volumes/Casa/dev/dissertation/_chaps), and [`_apps/`](/Volumes/Casa/dev/dissertation/_apps): manuscript source, analysis chunks, and appendix material.

What this stage produces:

- a direct Quarto PDF rebuild
- a direct Quarto HTML/book rebuild
- manuscript-facing outputs under the current source tree

How to run it today:

PDF:

```bash
quarto render --to pdf --profile pdf
```

HTML:

```bash
quarto render --to html --profile html
```

Canonical artifact rule:

- manuscript artifact: [`defended-2024-08-02/main.pdf`](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf)
- deposited package: [`defended-2024-08-02/oleary-2024-08-02.pdf`](/Volumes/Casa/dev/dissertation/defended-2024-08-02/oleary-2024-08-02.pdf)
- IRB packet: [`defended-2024-08-02/irb.pdf`](/Volumes/Casa/dev/dissertation/defended-2024-08-02/irb.pdf)

Current reproducibility status:

- the Quarto PDF and HTML paths both rebuild successfully
- the current source tree now renders the PDF front matter directly without the earlier empty/duplicate chapter artifact
- the current direct PDF rebuild is a near-match to `main.pdf`, not a perfect rendered replica; apart from the already documented text-level deltas, newer Quarto / Pandoc / LaTeX versions introduce line-break, hyphenation, and pagination drift
- the HTML profile includes a separate unnumbered `Acknowledgements` chapter between `Abstract` and `Introduction`

## What Another Researcher Can Reasonably Reproduce Today

A technically capable researcher can reasonably:

- inspect the preserved source materials and external-archive provenance
- rerun the active Python extraction step against the UNAS archive
- verify hash-matching extraction outputs
- inspect and partially rerun the R curation logic
- rebuild the manuscript PDF and HTML outputs from the preserved curated artifacts

What remains caveated:

- exact byte-for-byte reproduction of [`data/combined_results.xlsx`](/Volumes/Casa/dev/dissertation/data/combined_results.xlsx), because XLSX writer/container serialization can drift even when the workbook contents read back identically
- exact rendered reproduction of canonical [`main.pdf`](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf), because the current rebuild remains a near-match rather than a byte- or layout-identical replica even after fixing the earlier front-matter issue
- a fully self-contained workflow with no external archive dependency

## Related Notes

- [data.md](/Volumes/Casa/dev/dissertation/docs/data.md): detailed provenance and artifact relationships
- [thunderbay-inventory.md](/Volumes/Casa/dev/dissertation/docs/thunderbay-inventory.md): external archive structure and verified UNAS replica
- [parse_xml/README.md](/Volumes/Casa/dev/dissertation/parse_xml/README.md): active extraction entry point
- [analysis/forms_data/README.md](/Volumes/Casa/dev/dissertation/analysis/forms_data/README.md): active R curation step
- [build.md](/Volumes/Casa/dev/dissertation/docs/build.md): manuscript build path and artifact caveats
- [r-environment-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/r-environment-2026-03-12.md): current working R environment snapshot

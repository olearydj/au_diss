# R Environment Capture (2026-03-12)

## Purpose

This note captures the arm64 R environment that successfully rebuilt the dissertation on March 12, 2026 and records how that capture was later promoted into the modern rebuild lock on March 13, 2026.

The resulting root `renv.lock` should be interpreted as the operational lock for the modern rebuildable line, not as a claim about the exact defended-era package state.

## Captured Artifacts

- Original capture lock snapshot: `docs/renv-baseline-2026-03-12.lock`
- Promoted modern rebuild lock: `renv.lock`
- Archived pre-promotion root lock: `docs/renv-historical-root.lock`
- Package manifest: `docs/r-package-manifest-2026-03-12.csv`
- Session metadata: `docs/r-session-info-2026-03-12.txt`

## Capture Context

- R version: `4.4.0`
- Platform: `aarch64-apple-darwin20`
- Current project library:
  `renv/library/macos/R-4.4/aarch64-apple-darwin20`
- Installed package count in that library: `240`

## Capture Method

The March 12 capture was produced without overwriting the then-existing root `renv.lock`.

Because non-interactive `source("renv/activate.R")` was not reliable in this shell, the capture used `Rscript --vanilla` with `.libPaths()` pointed directly at the current project library, then ran `renv::snapshot(...)` against that library.

Operationally, the March 12 capture produced:

- a machine-readable package manifest from the current library
- a plain `sessionInfo()` record
- a machine-readable lock snapshot for that current successful-build environment

## Interpretation

The March 12 capture should be treated as a **current reproducibility snapshot**, not as a proven historical bill of materials.

Reasons:

- The successful arm64 build environment was reconstructed from a mixture of:
  - the existing historical `renv.lock`
  - frozen Posit Package Manager installs
  - Intel-library forensics from the preserved old `renv` tree
  - targeted package pinning during rebuild
- The alternate lock snapshot records mixed repository provenance:
  - top-level repo URL: `https://cloud.r-project.org`
  - many packages recorded with repository `RSPM`
  - `20` packages recorded explicitly from `https://packagemanager.posit.co/cran/2025-07-31`
- `renv::snapshot(...)` completed successfully, but it also warned that the broader repo still references packages not installed in the current project library. That is expected here because the lockfile/buildable manuscript path and the full exploratory repo contents are not the same thing.

## Promotion Addendum (2026-03-13)

The March 12 snapshot was later promoted into the root `renv.lock` for the modern rebuildable line.

That promotion required two clarifications:

- the previous root `renv.lock` was archived as `docs/renv-historical-root.lock`
- the implicit March 12 snapshot had missed two build-time packages that were present in the working arm64 library but not recorded in the lock:
  `modelbased 0.8.7` and `see 0.8.4`

After promoting the lock and adding those two package records from the working arm64 library, the modern rebuild lock was revalidated in a clean temporary arm64 library:

- `renv::restore()` completed successfully from the promoted root `renv.lock`
- `analysis/forms_data/forms_data.Rmd` reran successfully
- the regenerated QA CSVs under `analysis/forms_data/output/` hash-matched the preserved local reference outputs exactly
- the regenerated `data/combined_results.xlsx` workbook read back identically through `readxl`, while the raw XLSX hash still drifted because spreadsheet container serialization is not byte-stable
- `quarto render --to pdf --profile pdf` succeeded
- `quarto render --to html --profile html` succeeded

## Current Interpretation

For the modern rebuildable line:

- root `renv.lock` is the operational lockfile future users should restore from
- `docs/renv-historical-root.lock` preserves the old pre-promotion root lock as historical evidence
- `docs/renv-baseline-2026-03-12.lock` remains the original March 12 capture artifact that informed the later promoted root lock
- `docs/r-package-manifest-2026-03-12.csv` and `docs/r-session-info-2026-03-12.txt` remain the plain-language audit trail for the captured arm64 library

The March 12 capture already incorporated the `downlit`, `brio`, and `desc` additions required for the verified HTML-capable environment. The March 13 promotion completed that capture for full rebuild use by adding the missing `modelbased` and `see` records.

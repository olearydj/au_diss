# R Environment Capture (2026-03-12)

## Purpose

This note captures the current arm64 R environment that successfully rebuilt the dissertation on March 12, 2026.

It is intentionally separate from the repository's historical `renv.lock`. The goal is to preserve the currently working build environment without claiming that it is the exact defended-era package state.

## Captured Artifacts

- Alternate lock snapshot: `docs/renv-baseline-2026-03-12.lock`
- Package manifest: `docs/r-package-manifest-2026-03-12.csv`
- Session metadata: `docs/r-session-info-2026-03-12.txt`

## Capture Context

- R version: `4.4.0`
- Platform: `aarch64-apple-darwin20`
- Current project library:
  `renv/library/macos/R-4.4/aarch64-apple-darwin20`
- Installed package count in that library: `240`

## Capture Method

The project library was captured without overwriting the existing `renv.lock`.

Because non-interactive `source("renv/activate.R")` was not reliable in this shell, the capture used `Rscript --vanilla` with `.libPaths()` pointed directly at the current project library, then ran `renv::snapshot(...)` against that library.

Operationally, this produced:

- a machine-readable package manifest from the current library
- a plain `sessionInfo()` record
- an alternate `renv` lock snapshot for the current successful-build environment

## Interpretation

This snapshot should be treated as a **current reproducibility snapshot**, not as a proven historical bill of materials.

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

## Baseline Implication

For current baselining work:

- keep the existing top-level `renv.lock` unchanged
- treat `docs/renv-baseline-2026-03-12.lock` as support material for the verified current rebuild
- use `docs/r-package-manifest-2026-03-12.csv` and `docs/r-session-info-2026-03-12.txt` as the plain-language audit trail for that snapshot

The later baseline decision is whether this alternate lock snapshot should become canonical support material, remain documentary only, or be normalized further before promotion.

## Post-Capture Change

After this snapshot was taken, `downlit` was installed into the project library so the HTML/book render would complete without the prior code-link warning.

That means:

- the dissertation PDF rebuild evidence captured here is still valid
- the verified HTML render path is now in a better state than this snapshot records
- if the alternate lock snapshot is later promoted to canonical support material, it should either be refreshed or accompanied by a note that the final verified HTML-capable environment also includes `downlit`

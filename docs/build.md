# Build And Provenance

## Purpose

This note records the dissertation build path that should be treated as canonical during repository baselining.

## Canonical Outputs

- Manuscript artifact: `defended-2024-08-02/main.pdf`
- Deposited package artifact: `defended-2024-08-02/oleary-2024-08-02.pdf`
- IRB packet used in deposit assembly: `defended-2024-08-02/irb.pdf`

These roles are defined in `docs/artifacts.md`.

## Historical Workflow

Current evidence supports this publication path:

1. Render the Quarto book to produce the manuscript PDF.
2. Post-process that PDF to correct the front-matter / empty-chapter artifact produced by the direct render.
3. Use the corrected manuscript PDF as `main.pdf`.
4. Combine `main.pdf` with the separately produced IRB packet to create the deposited package PDF.

The exact historical post-processing step has not been fully reconstructed. On the current machine, simply deleting page 1 from the rebuilt PDF improves the front matter but does not fully recreate `main.pdf`, so the old environment or post-processing path was likely slightly different.

## Current Source Build

Main Quarto config:

- `_quarto.yml`

Historical manual full/partial-build config variants have been archived under
`archive/quarto-config-variants/`. They document drafting-era workflow
experiments but are not part of the active source build.

Primary render command:

```sh
quarto render --to pdf --profile book
```

Current PDF config characteristics:

- output directory: `manuscript/`
- observed rebuild output path:
  `manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf`
- PDF engine: LuaLaTeX via Quarto
- bibliography path: `references.bib`
- custom template: `tex/template.tex`
- generated TeX retained: `keep-tex: true`

The same Quarto config also defines an HTML output path for website/book-style rendering. That path was revalidated on the current machine using a disposable output directory:

```sh
quarto render --to html --output-dir html
```

Observed result:

- the HTML/book render succeeds
- the generated site is coherent and includes the active chapter and appendix set from `_quarto.yml`
- `downlit` is now installed in the project library, so the previous code-link warning is resolved
- `css/custom.css` now overrides the newer Bootstrap inline-code background so the rebuilt HTML matches the older light inline-code pill appearance
- the top-level `html/` directory is treated as generated-on-demand and ignored in git
- a preserved HTML snapshot is kept at `defended-2024-08-02/html/`

## Data Workflow Note

The dissertation data pipeline is not completely uniform across all three phases of the study.

- The main curated workbook, `data/combined_results.xlsx`, was produced by the original Excel/R/Python aggregation path and covers the phase 1 / phase 2 study data exported in `analysis/forms_data/forms_data.Rmd`.
- That export path explicitly stopped short of incorporating phase 3 retention data; `analysis/forms_data/forms_data.Rmd` still carries a TODO to "add phase 3".
- The retention/H3 analysis instead reads `data/source/i1_h3.xlsx` directly and joins it to `demographics` from `combined_results.xlsx` and recall-derived objects from `rdata/`.
- Current evidence and author confirmation indicate this happened because the H3 analysis was deferred and then completed later in a more ad hoc way, rather than being folded back into the original workbook-generation pipeline.

This means the current baseline should treat `data/source/i1_h3.xlsx` as a legitimate source artifact for the retention analysis, not as an anomalous duplicate of `combined_results.xlsx`.

Related preserved support artifacts:

- `data/source/notes/` contains participant-level script notes and feedback
- `data/reports/` contains generated participant reports that relate those notes to workbook/video metadata

The fuller source-to-curated workflow, including the external video/XML roots and the Python-to-R handoff through `data/csv/i1_times_v2.csv`, is documented in `docs/data.md`.

Those directories are not active build inputs, but they are part of the preserved research record.

## Current Rebuild State

The current machine has already been shown to render the dissertation successfully through the full Quarto/R/LaTeX/Biber path.

Current build interpretation:

- The rebuilt manuscript is practically equivalent to `main.pdf`.
- The remaining known differences are documented, not ignored.
- The main unresolved render artifact is the phantom front-matter / empty-chapter effect.

Release-prep validation on March 13, 2026 also confirmed the modern rebuild lock end to end:

- a clean temporary arm64 `renv::restore()` succeeded from the promoted root `renv.lock`
- `analysis/forms_data/forms_data.Rmd` reran successfully from that restored library
- the regenerated QA CSVs matched the preserved local reference hashes exactly
- the regenerated `data/combined_results.xlsx` workbook remained logically identical by `readxl`, while the raw XLSX hash still drifted at the container level
- both the PDF and HTML Quarto render paths succeeded from that restored library

## Known Rebuild Caveats

1. Direct current render still emits an extra front-matter page / empty chapter effect.
2. Current rebuild does not fully reproduce the exact historical post-processing step that yielded `main.pdf`.
3. The current package stack can inject runtime output into the Results chapter if a chunk does not suppress emitted output.
4. The deposited package is a separate artifact class from the manuscript PDF and should not be treated as a plain re-render of the book.
5. The HTML build now succeeds cleanly with `downlit` installed and the regenerated `html/` output matches the active chapter and appendix set.

## Remaining Ignored Residue

The remaining ignored worktree now consists mostly of render residue, QA/debug outputs, parser test fixtures, and local editor noise. That audit is documented in `docs/worktree-audit.md`.

## Content-Level Baseline Rule

For current baselining work, treat the current source tree as the effective archival source, with only the documented deltas listed in `docs/text-content-diff.md`.

## Environment Capture Artifacts

The current successful-build environment was first captured separately and then promoted into the modern rebuild lock:

- Operational modern rebuild lock: [renv.lock](/Volumes/Casa/dev/dissertation/renv.lock)
- Archived pre-promotion root lock: [renv-historical-root.lock](/Volumes/Casa/dev/dissertation/docs/renv-historical-root.lock)

- R snapshot note: [r-environment-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/r-environment-2026-03-12.md)
- Original March 12 lock snapshot: [renv-baseline-2026-03-12.lock](/Volumes/Casa/dev/dissertation/docs/renv-baseline-2026-03-12.lock)
- R package manifest: [r-package-manifest-2026-03-12.csv](/Volumes/Casa/dev/dissertation/docs/r-package-manifest-2026-03-12.csv)
- R session metadata: [r-session-info-2026-03-12.txt](/Volumes/Casa/dev/dissertation/docs/r-session-info-2026-03-12.txt)
- TeX footprint note: [tex-package-footprint-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/tex-package-footprint-2026-03-12.md)

The March 12 capture snapshot missed two build-time packages that were present in the working arm64 library but not recorded by the implicit snapshot. The promoted root `renv.lock` was therefore completed with `modelbased 0.8.7` and `see 0.8.4` before clean restore validation.

## Next Build-Related Work

The next build-focused tasks are:

1. decide the eventual modern rebuild tag name and release description
2. decide which rebuilt HTML/PDF artifacts should ship alongside that tag
3. decide whether the March 12 capture lock should remain documentary support material once the promoted root lock is published

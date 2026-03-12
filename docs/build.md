# Build And Provenance

## Purpose

This note records the dissertation build path that should be treated as canonical during repository baselining.

## Canonical Outputs

- Manuscript artifact: `_versions/submitted-2024-08-02/main.pdf`
- Deposited package artifact: `_versions/submitted-2024-08-02/oleary-2024-08-02.pdf`
- IRB packet used in deposit assembly: `_versions/submitted-2024-08-02/irb.pdf`

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
- the top-level `html/` directory has been regenerated from the current active source set and no longer includes the previously stale extra pages

## Current Rebuild State

The current machine has already been shown to render the dissertation successfully through the full Quarto/R/LaTeX/Biber path.

Current build interpretation:

- The rebuilt manuscript is practically equivalent to `main.pdf`.
- The remaining known differences are documented, not ignored.
- The main unresolved render artifact is the phantom front-matter / empty-chapter effect.

## Known Rebuild Caveats

1. Direct current render still emits an extra front-matter page / empty chapter effect.
2. Current rebuild does not fully reproduce the exact historical post-processing step that yielded `main.pdf`.
3. The current package stack can inject runtime output into the Results chapter if a chunk does not suppress emitted output.
4. The deposited package is a separate artifact class from the manuscript PDF and should not be treated as a plain re-render of the book.
5. The HTML build now succeeds cleanly with `downlit` installed and the regenerated `html/` output matches the active chapter and appendix set.

## Content-Level Baseline Rule

For current baselining work, treat the current source tree as the effective archival source, with only the documented deltas listed in `docs/text-content-diff.md`.

## Environment Capture Artifacts

The current successful-build environment is now documented separately from the historical source lockfile:

- R snapshot note: [r-environment-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/r-environment-2026-03-12.md)
- Alternate R lock snapshot: [renv-baseline-2026-03-12.lock](/Volumes/Casa/dev/dissertation/docs/renv-baseline-2026-03-12.lock)
- R package manifest: [r-package-manifest-2026-03-12.csv](/Volumes/Casa/dev/dissertation/docs/r-package-manifest-2026-03-12.csv)
- R session metadata: [r-session-info-2026-03-12.txt](/Volumes/Casa/dev/dissertation/docs/r-session-info-2026-03-12.txt)
- TeX footprint note: [tex-package-footprint-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/tex-package-footprint-2026-03-12.md)

These artifacts capture the current verified rebuild environment without overwriting the repository's historical `renv.lock`.

## Next Build-Related Work

The next build-focused tasks are:

1. decide whether the captured R environment should become canonical baseline support material
2. decide whether the updated alternate R snapshot should remain documentary support material or be promoted later
3. complete generated-noise triage and archival cleanup before the baseline commit

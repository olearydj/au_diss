# Dissertation Repository

This repository is the working archive for the dissertation:

*Augmented vs. Traditional Instruction in Manufacturing Assembly: An Affordance-Based, Multi-Modal Assessment of Learning, Recall, and Retention*

The dissertation is complete and defended. This repository is being baseline-cleaned so it can serve as the archival source for future publication work.

## Canonical Artifacts

- Canonical manuscript artifact: `_versions/submitted-2024-08-02/main.pdf`
- Canonical deposited package artifact: `_versions/submitted-2024-08-02/oleary-2024-08-02.pdf`
- Canonical IRB appendix packet: `_versions/submitted-2024-08-02/irb.pdf`

These artifact roles are documented in `docs/artifacts.md`.

## Current Baseline Rule

For baselining purposes, the current source tree is treated as the effective archival source, with three documented text-level deltas from the canonical manuscript artifact:

1. A post-submission wording correction in Acknowledgements.
2. A rebuilt-only `compare_performance(...)` warning injected into the Results chapter by the current package stack.
3. A missing `January` in one bibliography entry under the current bibliography rendering stack.

Details are recorded in `docs/text-content-diff.md`.

## Historical Build/Deposit Path

The current understanding of the historical publication workflow is:

1. Render the Quarto book to produce the manuscript PDF.
2. Post-process the manuscript PDF to correct the front-matter / empty-chapter artifact.
3. Combine the corrected manuscript PDF with the separately produced IRB packet to create the deposited package.

This is documented in `docs/build.md`.

## Repository Layout

- `_front/`: written frontmatter source.
- `_chaps/`: main dissertation chapters and some exploratory chapter-side work.
- `_apps/`: appendices and appendix-source material.
- `data/`: curated spreadsheets, reports, and supporting data artifacts.
- `archive/`: non-baseline exploratory, drafting, and historical materials retained for provenance.
- `rdata/`: saved R objects used by the analysis and manuscript build.
- `parse_xml/`: Python utilities for processing annotation exports and derived reports.
- `tex/`: custom LaTeX template work and Quarto template experiments.
- `manuscript/`: current render output directory.
- `_versions/`: archived submission-era artifacts.
- `docs/`: baseline, rebuild, artifact, and provenance notes for repository cleanup.

Retention/H3 data note:

- `data/combined_results.xlsx` is the curated main-study workbook produced by the original data pipeline for phases 1 and 2.
- `data/source/i1_h3.xlsx` is a separate retention-phase support workbook used by the later H3 analysis.
- Current evidence indicates H3 was analyzed later and more ad hoc, rather than being folded back into the original Excel/Python aggregation workflow.
- `data/source/notes/` holds participant-level source notes and feedback markdown.
- `data/reports/` holds generated participant reports derived from the source notes, workbook data, and local video metadata.

## Build

The main manuscript build is driven by `_quarto.yml`.

Primary render command:

```sh
quarto render --to pdf --profile book
```

The current repository already includes `keep-tex: true` in the PDF format config so generated TeX is preserved during PDF builds.

The same Quarto project also includes an HTML render path. That website/book output has now been re-verified on the current machine using:

```sh
quarto render --to html --output-dir html
```

Current HTML verification notes:

- the book/site render succeeds
- the generated site output is coherent and includes the active chapter and appendix set from `_quarto.yml`
- `downlit` is now installed in the project library, so HTML code-linking no longer emits the prior missing-package warning
- `css/custom.css` now restores the older light inline-code background used by the archived HTML output
- the top-level `html/` tree has been regenerated from the current active source set and no longer includes the previously stale extra pages

Build notes, historical caveats, and current reproducibility status are in `docs/build.md` and `docs/rebuild-checklist.md`.

## Documentation

- `docs/artifacts.md`: canonical artifacts and source-state rules.
- `docs/build.md`: build path, provenance, and current known caveats.
- `docs/baseline-plan.md`: overall cleanup/baseline plan.
- `docs/data.md`: data-tree provenance and relationships between raw, curated, generated, and archival analysis inputs.
- `docs/rebuild-checklist.md`: rebuild verification notes and environment findings.
- `docs/text-content-diff.md`: content-only comparison between `main.pdf` and the rebuilt manuscript.
- `docs/intel-renv-manifest.md`: recovered package evidence from the preserved Intel `renv` library.
- `docs/r-environment-2026-03-12.md`: current arm64 R environment snapshot and alternate lockfile notes.
- `docs/tex-package-footprint-2026-03-12.md`: actual LaTeX package footprint extracted from the successful build artifacts.
- `docs/tex-dependencies.md`: TeX-side dependency notes discovered during rebuild.

## Status

The repository is not yet at its final archival baseline. The current branch is being used to:

1. define canonical artifacts and rules
2. document the build and deposit path
3. capture the current reproducible R and TeX environment
4. clean generated noise and commit the archival baseline

# Repository Guide

This note preserves the longer-form repository overview that used to live in the
root README.

It is meant for readers who want more context about repository layout, artifact
roles, build behavior, and current status than a GitHub landing page should
carry.

## Repository Role

This repository is the working archive for the dissertation:

*Augmented vs. Traditional Instruction in Manufacturing Assembly: An
Affordance-Based, Multi-Modal Assessment of Learning, Recall, and Retention*

The dissertation is complete and defended. This repository now preserves both
the defended archival baseline and a modern rebuildable research snapshot for
follow-on publication work.

## Canonical Artifacts

Canonical artifact roles are:

- canonical manuscript artifact: local defended snapshot `main.pdf`
- canonical deposited package artifact: local defended snapshot
  `oleary-2024-08-02.pdf`
- canonical IRB appendix packet:
  [`defended-2024-08-02/irb.pdf`](../defended-2024-08-02/irb.pdf)

Large defended PDFs are not stored as normal git blobs on GitHub because they
exceed GitHub's file size limit. The defended baseline release is the right
public distribution point for those oversized canonical artifacts.

Artifact roles and source-state rules are documented in
[`artifacts.md`](artifacts.md).

## Current Baseline Rule

For baselining purposes, the current source tree is treated as the effective
archival source, with three documented text-level deltas from the canonical
manuscript artifact:

1. A post-submission wording correction in Acknowledgements.
2. A rebuilt-only `compare_performance(...)` warning injected into the Results
   chapter by the current package stack.
3. A missing `January` in one bibliography entry under the current bibliography
   rendering stack.

Details are recorded in
[`text-content-diff.md`](text-content-diff.md).

## Historical Build And Deposit Path

The current understanding of the historical publication workflow is:

1. Render the Quarto book to produce the manuscript PDF.
2. Post-process the manuscript PDF to correct the front-matter / empty-chapter
   artifact.
3. Combine the corrected manuscript PDF with the separately produced IRB packet
   to create the deposited package.

This is documented in
[`build.md`](build.md).

## Rebuild Snapshot

- historical defended state:
  `baseline/dissertation-defended-2024-08-02`
- modern rebuild state:
  `rebuild/dissertation-arm64-verified-2026-03-13`
- current working line:
  `master`
- archived pre-promotion root lock:
  [`renv-historical-root.lock`](renv-historical-root.lock)

The modern rebuild lock was promoted from the March 12, 2026 environment capture
and then completed with the build-only package records required for a clean
restore and full Quarto rebuild.

## Repository Layout

- [`_front/`](../_front): written frontmatter source.
- [`_chaps/`](../_chaps): main active dissertation
  chapters; the integrated Results chapter lives here as
  [`_chaps/25-results.qmd`](../_chaps/25-results.qmd).
- [`_apps/`](../_apps): appendices and
  appendix-source material.
- [`data/`](../data): curated spreadsheets, reports,
  and supporting data artifacts.
- [`analysis/`](../analysis): active data-curation
  notebooks and their local QA outputs.
- [`archive/`](../archive): non-baseline
  exploratory, drafting, and historical materials retained for provenance,
  including archived Results-development drafts and historical Quarto config
  variants.
- [`rdata/`](../rdata): saved R objects used by the
  analysis and manuscript build.
- [`parse_xml/`](../parse_xml): active Python
  extraction utilities for annotation exports and derived reports.
- [`scripts/`](../scripts): small active project
  automation helpers, including the Quarto post-render cleanup hook.
- [`tex/`](../tex): custom LaTeX template work and
  Quarto template experiments.
- [`manuscript/`](../manuscript): current render
  output directory.
- [`defended-2024-08-02/`](../defended-2024-08-02):
  defended-era snapshot companion directory.
- [`docs/`](.): baseline, rebuild, artifact,
  and provenance notes for repository cleanup.

## Retention / H3 Note

- [`data/combined_results.xlsx`](../data/combined_results.xlsx)
  is the curated main-study workbook produced by the original data pipeline for
  phases 1 and 2.
- [`data/source/i1_h3.xlsx`](../data/source/i1_h3.xlsx)
  is a separate retention-phase support workbook used by the later H3 analysis.
- Current evidence indicates H3 was analyzed later and more ad hoc, rather than
  being folded back into the original Excel/Python aggregation workflow.
- [`data/source/notes/`](../data/source/notes)
  holds participant-level source notes and feedback markdown.
- [`data/reports/`](../data/reports) holds generated
  participant reports derived from the source notes, workbook data, and local
  video metadata.
- The original ThunderBay archive has been inventoried and copied to the UNAS
  Pro; details are in
  [`thunderbay-inventory.md`](thunderbay-inventory.md).

## Build

The main manuscript build is driven by
[`_quarto.yml`](../_quarto.yml).

Historical manual full/partial-build config variants have been archived under
[`archive/quarto-config-variants/`](../archive/quarto-config-variants).

Primary render command:

```sh
quarto render --to pdf --profile book
```

The current repository includes `keep-tex: true` in the PDF format config, and a
post-render helper moves the kept TeX file into
[`manuscript/`](../manuscript) so the repo root stays
clean.

The same Quarto project also includes an HTML render path:

```sh
quarto render --to html --output-dir html
```

Current HTML verification notes:

- the book/site render succeeds
- the generated site output is coherent and includes the active chapter and
  appendix set from [`_quarto.yml`](../_quarto.yml)
- `downlit` is installed in the project library, so HTML code-linking no longer
  emits the prior missing-package warning
- [`css/custom.css`](../css/custom.css) restores the
  older light inline-code background used by the archived HTML output
- the top-level `html/` tree is treated as generated-on-demand and ignored in
  git
- a preserved HTML snapshot lives under
  [`defended-2024-08-02/html/`](../defended-2024-08-02/html)

Build notes, historical caveats, and current reproducibility status are in
[`build.md`](build.md) and
[`rebuild-checklist.md`](rebuild-checklist.md).

## Documentation Index

- [`artifacts.md`](artifacts.md):
  canonical artifacts and source-state rules
- [`build.md`](build.md):
  build path, provenance, and current known caveats
- [`baseline-plan.md`](baseline-plan.md):
  overall cleanup/baseline plan
- [`pipeline.md`](pipeline.md):
  canonical end-to-end workflow note for the external archive, Python
  extraction, R curation, and manuscript build boundary
- [`data.md`](data.md):
  data-tree provenance and relationships between raw, curated, generated, and
  archival analysis inputs
- [`thunderbay-inventory.md`](thunderbay-inventory.md):
  read-only inventory of the surviving external ThunderBay archive and its
  relationship to the Python/video workflow
- [`worktree-audit.md`](worktree-audit.md):
  current ignored/generated residue and remaining cleanup decisions
- [`rebuild-checklist.md`](rebuild-checklist.md):
  rebuild verification notes and environment findings
- [`text-content-diff.md`](text-content-diff.md):
  content-only comparison between `main.pdf` and the rebuilt manuscript
- [`intel-renv-manifest.md`](intel-renv-manifest.md):
  recovered package evidence from the preserved Intel `renv` library
- [`r-environment-2026-03-12.md`](r-environment-2026-03-12.md):
  arm64 R environment capture, lock-promotion notes, and release-prep
  verification summary
- [`renv-historical-root.lock`](renv-historical-root.lock):
  archived pre-promotion root `renv.lock`
- [`tex-package-footprint-2026-03-12.md`](tex-package-footprint-2026-03-12.md):
  actual LaTeX package footprint extracted from successful build artifacts
- [`tex-dependencies.md`](tex-dependencies.md):
  TeX-side dependency notes discovered during rebuild

## Status

The archival defended baseline is established on:

- branch: `master`
- tag: `baseline/dissertation-defended-2024-08-02`

Current follow-on work happens on focused task branches created from `master` as
needed. The active root
[`renv.lock`](../renv.lock) is now intended to
support the modern rebuildable line rather than preserve the older historical
root lock in place.

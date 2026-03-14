# Dissertation Repository

This repository preserves the source workspace for the dissertation:

*Augmented vs. Traditional Instruction in Manufacturing Assembly: An Affordance-Based, Multi-Modal Assessment of Learning, Recall, and Retention*

It now serves three related purposes:

- archival source-state reference for the defended dissertation
- verified modern rebuild snapshot for reproducibility work
- continuing workspace for cleanup and publication-oriented follow-on research

## Which Version To Use

- `baseline/dissertation-defended-2024-08-02`
  - the defended archival baseline
- `rebuild/dissertation-arm64-verified-2026-03-13`
  - the verified modern rebuild snapshot for current arm64/macOS work
- `master`
  - the current working line for ongoing repository improvements

## Artifacts

The defended dissertation artifacts are not all stored as normal git blobs on
GitHub because the PDFs exceed GitHub's 100 MB file limit.

- Baseline release:
  [baseline/dissertation-defended-2024-08-02](https://github.com/olearydj/au_diss/releases/tag/baseline/dissertation-defended-2024-08-02)
- In-repo defended snapshot companion material:
  [`defended-2024-08-02/`](defended-2024-08-02/)

Canonical artifact roles are documented in
[`docs/artifacts.md`](docs/artifacts.md).

## Quick Start

Read the end-to-end workflow note first:

- [`docs/pipeline.md`](docs/pipeline.md)

Build the current manuscript PDF:

```sh
quarto render --to pdf --profile pdf
```

Build the current HTML version:

```sh
quarto render --to html --profile html
```

The current PDF output lands at `manuscript/dissertation.pdf`. The kept TeX
file is moved to `manuscript/dissertation.tex`. The HTML build lands at
`html/`.

## Key Docs

- [`docs/repository-guide.md`](docs/repository-guide.md): fuller repository overview, build story, layout, and status notes
- [`docs/pipeline.md`](docs/pipeline.md): canonical end-to-end workflow note
- [`docs/build.md`](docs/build.md): build path and current caveats
- [`docs/data.md`](docs/data.md): data provenance and artifact relationships
- [`docs/text-content-diff.md`](docs/text-content-diff.md): documented differences between the canonical manuscript artifact and the current direct rebuild
- [`docs/rebuild-checklist.md`](docs/rebuild-checklist.md): rebuild verification notes

## Repository Layout

- [`_chaps/`](_chaps/): active chapter source
- [`_apps/`](_apps/): appendices and appendix-source material
- [`analysis/`](analysis/): active curation notebooks and local QA outputs
- [`data/`](data/): curated spreadsheets, reports, and supporting data artifacts
- [`parse_xml/`](parse_xml/): active Python extraction step
- [`archive/`](archive/): preserved inactive drafts, legacy pipeline generations, and historical workflow material

## Notes

- The current direct PDF rebuild is a near-match to the canonical defended manuscript, not a perfect rendered replica.
- The current source tree now renders corrected PDF front matter directly; the remaining rebuild differences are documented in `docs/text-content-diff.md` and `docs/build.md`.
- The active root [`renv.lock`](renv.lock) is intended to support the modern rebuildable line, not preserve the older historical root lock in place.

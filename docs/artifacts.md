# Artifact Definitions

## Canonical Artifacts

These files are the authoritative dissertation-era artifacts for baselining.

### Manuscript Artifact

- Path: `_versions/submitted-2024-08-02/main.pdf`
- Role: canonical dissertation manuscript artifact
- Page count class: `304`
- Notes:
  - this is the primary comparison target for manuscript content
  - this is the artifact the current Quarto/R/LaTeX build should be judged against

### Deposited Package Artifact

- Path: `_versions/submitted-2024-08-02/oleary-2024-08-02.pdf`
- Role: canonical deposited package artifact
- Page count class: `427`
- Notes:
  - this is not just the manuscript PDF with different metadata
  - this is a larger package artifact that includes appended material beyond the dissertation body

### IRB Packet

- Path: `_versions/submitted-2024-08-02/irb.pdf`
- Role: separately produced IRB appendix packet used in deposit assembly
- Page count class: `123`
- Notes:
  - this appears to have been appended to the manuscript artifact to create the deposited package

## Supporting Non-Canonical Comparison Artifacts

These are useful for reconstruction but should not be treated as the canonical baseline targets.

### Current Render Output

- Path: `manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf`
- Role: current successful rebuild output on the active cleanup branch

### Rebuilt Minus Page 1

- Path: `_build-compare/rebuilt-minus-page1.pdf`
- Role: comparison helper used to evaluate the historical front-matter/post-processing behavior

### Defended Reference Copy

- Path: `_build-compare/defended-reference.pdf`
- Role: preserved local comparison copy used during rebuild investigation

## Canonical Source State

For current baselining work, the current source tree is treated as the effective archival source.

This rule comes with three documented text-level deltas from the canonical manuscript artifact `main.pdf`:

1. Acknowledgements wording in `_front/13-acknowledgements.qmd`
2. Rebuilt-only `compare_performance(...)` warning emitted into the Results chapter during current rendering
3. Missing `January` in one rendered reference entry under the current bibliography stack

Those deltas are documented in `docs/text-content-diff.md`.

## Artifact Lineage

Current evidence supports this lineage:

1. Quarto render produced the manuscript PDF.
2. The manuscript PDF was post-processed to correct the front-matter / empty-chapter artifact.
3. The corrected manuscript became `main.pdf`.
4. `main.pdf` was combined with `irb.pdf` to create `oleary-2024-08-02.pdf`.

## Baselining Rule

Until later cleanup work says otherwise:

- treat `main.pdf` as the canonical manuscript target
- treat `oleary-2024-08-02.pdf` as the canonical deposited package target
- treat the current source tree as the archival source, subject only to the three documented deltas above

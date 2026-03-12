# Text Content Diff

This document records a content-only comparison between the submitted manuscript PDF and the current rebuilt manuscript PDF.

Compared artifacts:

- Submitted manuscript: `_versions/submitted-2024-08-02/main.pdf`
- Current rebuild, with the phantom first page removed during comparison

Excluded from scope:

- generated TOC / LOF / LOT pages
- appendices
- PDF links, layout, pagination, line breaks, hyphenation, chapter-number drift, and similar rendering artifacts

Included in scope:

- written frontmatter
- main chapters
- references

## Method

The comparison was done by extracting text from the two PDFs and normalizing:

- whitespace and line wrapping
- hyphenation artifacts introduced by PDF extraction
- chapter / section / table / figure numbering drift
- bibliography backreferences such as `cit. on p. ...`

Where the PDF comparison remained noisy because of tables, figures, captions, or extraction order, the text was cross-checked against current source files and the submission-era git history.

## Findings

### Frontmatter

Title page and abstract content match after normalization.

One real wording difference was found in the Acknowledgements:

- `main.pdf`: `introduced me many of the tools that made this possible`
- rebuilt: `introduced me to many of the tools that made this possible`

Relevant source:

- `_front/13-acknowledgements.qmd`

This is a genuine text difference, not a rendering artifact.

### Introduction

No substantive text differences found.

Observed differences were hyphenation / extraction noise, e.g. `AR-assisted` vs `ARassisted`.

Relevant source:

- `_chaps/21-intro.qmd`

### Literature Review

No substantive prose drift was found.

Apparent differences are caused by PDF extraction order around:

- figure captions
- footnotes / sidenote-style material
- inline references and URLs

Relevant source:

- `_chaps/22-lit_review.qmd`

### Problem Statement

No substantive text differences found.

Observed differences were limited to hyphenation / extraction noise, e.g. `paper-based` vs `paperbased`.

Relevant source:

- `_chaps/23-prob_statement.qmd`

### Methods

No substantive chapter-text differences were confirmed between the two PDFs.

There are current source edits in `_chaps/24-methods.qmd`, but direct checks against both PDFs showed the visible manuscript text still aligns on the sampled passages that looked suspicious in raw extraction.

Most apparent differences in this chapter are caused by:

- figure / caption extraction order
- equation numbering drift
- URLs and footnotes being extracted differently

Relevant source:

- `_chaps/24-methods.qmd`

### Results

No substantive prose drift was confirmed in the narrative text.

One real rebuilt-only textual artifact was found near the model-performance table:

- rebuilt includes:
  `Random effect variances not available. Returned R2 does not account for random effects.`
- `main.pdf` does not include this warning text
- the source chapter does not contain this warning text

This is a build-time warning injected by the current package stack during rendering, not a source-text difference.

Mechanism:

- the source chunk at `_chaps/25-results.qmd` computes `cp_h1b_uc <- compare_performance(...)`
- that chunk does not suppress emitted output with chunk options
- under the current package stack, `compare_performance(...)` emits console text
- Quarto / knitr carries that output into the rendered document
- in the generated TeX, it appears as a literal verbatim block immediately before the table caption:
  `Random effect variances not available. Returned R2 does not account for random effects.`

Relevant source / artifacts:

- `_chaps/25-results.qmd`
- `Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.tex`

Relevant source:

- `_chaps/25-results.qmd`

### Conclusions

No substantive prose drift was found.

Visible differences are due to:

- chapter / section numbering drift from the phantom leading chapter
- line wrapping / hyphenation
- table extraction order

Cross-checks also confirmed that both PDFs match the current wording on the notable source-level phrase:

- `particularly between similar parts`

Relevant source:

- `_chaps/26-conclusions.qmd`

### References

After removing generated bibliography backreferences, one substantive bibliography-text difference remained:

- `main.pdf`: `Atkinson, R. C., & Shiffrin, R. M. (1968, January).`
- rebuilt: `Atkinson, R. C., & Shiffrin, R. M. (1968).`

The bibliography source includes `month = jan`, so this is a bibliography formatting / rendering difference, not a source-data omission.

Relevant source:

- `references.bib`

## Bottom Line

High confidence: the rebuilt manuscript and `main.pdf` contain the same substantive written content everywhere in scope except for these confirmed text differences:

1. Acknowledgements wording:
   `introduced me many` vs `introduced me to many`
2. Rebuilt-only warning text injected in Results near the model-performance table
3. References month omission for the Atkinson & Shiffrin entry

Everything else identified during comparison was attributable to rendering drift, extraction order, numbering drift, or bibliography backreference differences rather than changes to the dissertation's written content.

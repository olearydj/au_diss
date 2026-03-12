# Conclusions Delta Note

## Scope

This note compares the Conclusions chapter in:

- the rebuilt manuscript with the phantom first page removed during comparison
- [main.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf)

The goal is to identify real wording differences while excluding line-wrap, hyphenation, and page-layout noise.

## Result

No substantive prose drift was found in the Conclusions chapter.

Most visible differences are generated differences, not authorial text changes:

- section and table numbering are one high in the rebuilt PDF
- line breaks and hyphenation differ throughout the chapter
- the future-work table lays out differently across pages
- late in the chapter, pagination compresses by one page, causing References to begin earlier in the rebuilt PDF

## Confirmed Generated Differences

Examples seen in the rebuilt PDF versus `main.pdf`:

- `7.1.2 Survey Results` vs `6.1.2 Survey Results`
- `7.1.3 Qualitative Results` vs `6.1.3 Qualitative Results`
- `7.2 Conclusions` vs `6.2 Conclusions`
- `Table 7.5` vs `Table 6.5`
- `Section 6.6.3` vs `Section 5.6.3`
- `Section 6.7` vs `Section 5.7`

These differences are consistent with the known phantom front-matter chapter/page issue in the rebuild.

## Source Audit

The current source for the chapter is [_chaps/26-conclusions.qmd](/Volumes/Casa/dev/dissertation/_chaps/26-conclusions.qmd).

The paragraph cited during comparison at [_chaps/26-conclusions.qmd:25](/Volumes/Casa/dev/dissertation/_chaps/26-conclusions.qmd#L25) matches `main.pdf` in wording. The observed differences there are line-breaking and hyphenation only.

Two small source-level text differences were found in git history / working tree:

1. At [_chaps/26-conclusions.qmd:73](/Volumes/Casa/dev/dissertation/_chaps/26-conclusions.qmd#L73)
Current text:
`particularly between similar parts`

Earlier text:
`particularly in distinguishing similar parts`

`main.pdf` matches the current text.

2. At [_chaps/26-conclusions.qmd:160](/Volumes/Casa/dev/dissertation/_chaps/26-conclusions.qmd#L160)
Current text:
`(e.g., time pressures)`

Earlier committed text:
`(e.g. time pressures)`

`main.pdf` matches the current text.

## Conclusion

There is no evidence that `main.pdf` was built from a materially different Conclusions draft.

The apparent differences in Conclusions are best explained by:

- generated counter drift from the prelim/index/template structure
- TeX line-breaking and hyphenation differences
- table layout reflow
- one-page pagination compression near the end of the chapter

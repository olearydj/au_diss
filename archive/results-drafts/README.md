# Results Drafts

This folder preserves inactive Results-chapter development drafts that were previously kept in `_chaps/`.

They are not part of the active Quarto build. The active integrated Results chapter is `_chaps/25-results.qmd`.

These files appear to reflect a period when the Results chapter was split into smaller standalone drafts to make iteration cheaper while the full chapter was expensive to render. Most of that work was later folded back into the integrated chapter.

## How These Drafts Relate To `25-results.qmd`

- There is no active `include`, child-document, or similar wiring from these files into `_chaps/25-results.qmd`.
- Several drafts were designed to run as standalone analyses using saved `.RData` handoffs such as `shared.RData`, `learn.RData`, `res_f.RData`, and `recall.RData`.
- The integrated Results chapter later absorbed most of that logic directly, while still preserving some save/load boundaries for expensive fits and historical standalone use.

## Files

### `25-analysis.qmd`

- Original location: `_chaps/25-analysis.qmd`
- Status: exploratory notebook / early precursor
- Role:
  - quick ANOVA/Tukey-style treatment checks for recall elapsed time and error count
  - first-pass PWI reference analyses
  - early SUS/TLX treatment checks
  - early learning-rate exploration
- Relationship to the active Results chapter:
  - overlaps conceptually with the active H2, TLX/SUS, and H1b material
  - methods and framing were largely superseded rather than merged directly
  - retained because it shows an earlier, simpler analytic path and open questions

### `25a-h1a.qmd`

- Original location: `_chaps/25a-h1a.qmd`
- Status: superseded hypothesis draft
- Role:
  - standalone H1a analysis using repeated-measures mixed models on disaggregated task-time data
- Relationship to the active Results chapter:
  - only partially incorporated
  - the active chapter answers the same hypothesis, but uses aggregated participant averages and a non-parametric Kruskal-Wallis path instead
  - retained because it preserves a real abandoned analytic branch, not just redundant prose

### `25b-h1b.qmd`

- Original location: `_chaps/25b-h1b.qmd`
- Status: major precursor draft
- Role:
  - standalone H1b learning-rate development notebook
  - includes many alternate model formulations, failed starts, and comparison work
- Relationship to the active Results chapter:
  - core storyline and mature modeling work were folded into `_chaps/25-results.qmd`
  - much of the exploratory residue was not
  - retained because it documents how the final H1b path was reached

### `25c-h1c.qmd`

- Original location: `_chaps/25c-h1c.qmd`
- Status: largely incorporated draft
- Role:
  - standalone H1c average-error analysis using the `learn.RData` / `h1a.RData` handoff
- Relationship to the active Results chapter:
  - heavily incorporated into the integrated H1c section
  - retained mainly as a historical split-out chapter version

### `25d-h2.qmd`

- Original location: `_chaps/25d-h2.qmd`
- Status: heavily incorporated draft
- Role:
  - standalone recall-phase analysis
  - loads `res_f.RData` and `shared.RData`
  - writes `recall.RData`, `h2a_oee_boot_res.RData`, and `h2b_pwi_boot_res.RData`
- Relationship to the active Results chapter:
  - very close to a direct predecessor of the integrated H2 section
  - much of the code and structure was folded into `_chaps/25-results.qmd`
  - retained because it documents the split-phase workflow and `.RData` handoff design

### `25d-h3.qmd`

- Original location: `_chaps/25d-h3.qmd`
- Status: heavily incorporated draft
- Role:
  - standalone retention/H3 analysis
  - loads `shared.RData` and `recall.RData`
  - joins `data/source/i1_h3.xlsx` to `demographics` and recall-derived objects
- Relationship to the active Results chapter:
  - very heavily incorporated into the integrated H3 section
  - the active chapter still shows commented legacy load lines where the split-file handoff used to occur
  - retained because it preserves the original standalone H3 path

### `25-tlx.qmd`

- Original location: `_chaps/25-tlx.qmd`
- Status: heavily incorporated draft
- Role:
  - standalone TLX, SUS, and qualitative-feedback chapter
- Relationship to the active Results chapter:
  - very heavily incorporated into the integrated TLX/SUS/feedback section
  - retained because it cleanly captures the split-out user-experience analysis before reintegration

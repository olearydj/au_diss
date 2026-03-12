# Archive

This folder holds non-baseline materials that are worth preserving as part of the dissertation workspace history.

These files are not part of the active Quarto build and should not be treated as canonical manuscript source. They are retained because they capture real analysis, drafting, or historical context that may still be useful for future publication work.

## Contents

### `25-h1b-nonlinear.qmd`

- Original location: repo root
- Status: exploratory dead-end
- Role:
  - nonlinear learning-curve experiments for H1b
  - includes exponential, hyperbolic, and Gompertz mixed-effects attempts
- Relationship to manuscript:
  - not part of the active build
  - the main Results chapter later summarizes this line of work more briefly, noting that nonlinear forms were tried but had convergence issues

### `25-linear-pw.qmd`

- Original location: repo root
- Status: exploratory dead-end
- Role:
  - piecewise linear / segmented-learning model experiments for H1b
- Relationship to manuscript:
  - not part of the active build
  - corresponds to ideas raised in the split H1b development chapter but not carried into the final active Results path

### `25-m7r.qmd`

- Original location: `_chaps/25-m7r.qmd`
- Status: precursor draft
- Role:
  - robust-model validation and conditioned-model development around the `m7r` learning-rate analysis
- Relationship to manuscript:
  - much of this material was later merged into `_chaps/25-results.qmd`
  - retained here because it documents the intermediate formulation and interpretation work

### `h1b_mod_select.qmd`

- Original location: repo root
- Status: exploratory continuation
- Role:
  - spline and Bayesian alternatives explored after the main `m7r` draft
- Relationship to manuscript:
  - not part of the active build
  - referenced conceptually by the `25-m7r` draft as continuing model-selection work

### `chat.md`

- Original location: repo root
- Status: historical artifact
- Role:
  - prompt/summary scaffold used to begin ChatGPT 3.5 conversations during the H1b modeling work
- Relationship to manuscript:
  - not source content
- retained for archival/historical context

### `00-issues.md`

- Original location: repo root as `00-issues.qmd`
- Status: historical working note
- Role:
  - punch list of manuscript, template, and Quarto/RStudio issues from the writing/finalization period
- Relationship to manuscript:
  - not part of the active build
  - retained as historical context for unresolved or once-unresolved dissertation production issues

## Deleted Instead Of Archived

The following files were treated as scratch/debug residue rather than archival work products and were deleted:

- `_chaps/m7rc1_verbose_output.txt`
- `_temp.qmd`
- `temp.Rmd`
- `tables.md`
- `clean_packages.R`

Reason:

- `m7rc1_verbose_output.txt` appears to be optimizer/debug output from chasing a convergence issue.
- `_temp.qmd` and `temp.Rmd` are temporary analysis scraps with no clear role in the final manuscript or stable exploratory record.
- `tables.md` appears to be drafting scaffolding whose substantive contents were either incorporated elsewhere in the dissertation or superseded by later manuscript source.
- `clean_packages.R` was a destructive `renv` pruning utility whose logic relied on incomplete dependency discovery and likely contributed to lockfile/library drift; it was deleted to avoid future accidental use.

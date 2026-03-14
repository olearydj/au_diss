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

### `tbm-migration/`

- Original location: local untracked `scripts/` workspace files plus migration notes
- Status: archival operational reference
- Role:
  - helper scripts and notes from the completed ThunderBay -> UNAS copy/verification work
- Relationship to manuscript:
  - not part of the active dissertation build or curation pipeline
  - retained only because that migration now forms part of the provenance context for the surviving external archive

### `parse_xml-legacy/`

- Original location: `parse_xml/` plus root `requirements.txt`
- Status: archived inactive pipeline generations
- Role:
  - preserves the earlier Python XML/report-processing false starts that preceded the active `process_data.py` entry point
  - keeps the small XML fixture harness and legacy Python dependency record with those older scripts
- Relationship to manuscript:
  - not part of the active dissertation build or the active extraction switch-over
  - retained because it documents how the XML/report workflow evolved before settling on the surviving generation that produced `data/reports/` and `data/csv/i1_times_v2.csv`

### `results-drafts/`

- Original location: `_chaps/`
- Status: archived inactive Results-chapter development drafts
- Role:
  - preserves the exploratory notebook and split hypothesis/topic drafts that were used while the Results chapter was being developed in smaller pieces
  - captures the older `.RData` handoff pattern used by the split H1/H2/H3/TLX drafts
- Relationship to manuscript:
- not part of the active build
- most of the substantive work was later folded into `_chaps/25-results.qmd`
- retained because it documents how the integrated Results chapter was assembled and which analytic paths were superseded rather than merged directly

### `quarto-config-variants/`

- Original location: repo root as alternate `_quarto-*.yml` files
- Status: archived inactive build-helper configs
- Role:
  - preserves the manual full-build and partial-build Quarto configuration variants used while the dissertation was being written and long renders were being managed in smaller pieces
  - includes the older original config snapshot as historical reference
- Relationship to manuscript:
  - not part of the active build
  - the active manuscript build now uses only the root `_quarto.yml`
  - retained because it documents the drafting-era workaround for long builds

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

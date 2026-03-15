# Dissertation v1.1 Errata Checklist

Date: 2026-03-14

Status: working draft

Purpose:

- define the scope of the `v1.1` dissertation release
- convert the review findings into a concrete correction checklist
- separate required errata from optional future improvements
- provide release gates for the corrected HTML publication

This checklist is derived from the dissertation review completed on 2026-03-14 and is intended to guide the publication-safe `v1.1` release of the dissertation web version.

## Scope of v1.1

`v1.1` should be:

- an errata and cleanup release
- a methodological reconciliation release where the current manuscript is internally inconsistent
- a publication-safety release for the public HTML version

`v1.1` should not be:

- a quiet rewrite of the dissertation
- a new research project
- an excuse to add large new analyses unless they are required to correct misleading claims
- a full paper-extraction effort

## Release Outcome

The `v1.1` web dissertation should:

- correct known factual, editorial, and interpretive defects
- remove visible draft residue and non-public operational material
- explain material post-submission corrections plainly
- link back to the as-submitted dissertation for transparency

## Priority Levels

- `P0`: blocks any public `v1.1` release
- `P1`: required for a credible corrected dissertation
- `P2`: important quality improvement, but may be narrowed if needed
- `P3`: release packaging and transparency work

## P0: Publication Blockers

- [ ] Remove all visible TODOs, placeholders, and draft residue from active build chapters.
  - Current targets:
  - `_chaps/24-methods.qmd`
  - `_chaps/22-lit_review.qmd`
  - any appendix still included in the HTML build
- [ ] Eliminate visible warnings or printed model diagnostics from rendered chapter output.
  - Known issue:
  - injected model warning in Results
- [ ] Remove or sanitize Appendix H from publication-facing outputs.
  - Current target:
  - `_apps/38h-dataorg.qmd`
- [ ] Remove visible placeholder text such as `subtitle...` from Results.
  - Current target:
  - `_chaps/25-results.qmd`
- [ ] Fix obvious publication-facing copy defects in chapters that remain in `v1.1`.
  - Includes:
  - malformed words, repeated words, and obvious misspellings called out in the review

## P1: Internal Consistency and Correctness

### Methods and Results Reconciliation

- [ ] Rewrite the Methods retention/hypothesis material so it matches the actual Results chapter.
  - Current targets:
  - `_chaps/24-methods.qmd:337-349`
  - `_chaps/24-methods.qmd:357-390`
  - `_chaps/24-methods.qmd:1587-1624`
- [ ] Explain why OEE was abandoned for H3 and whether that change should be framed as corrective, exploratory, or post hoc.
- [ ] Ensure hypothesis labels, outcome names, and analysis descriptions match across Methods, Results, and Conclusions.

### Sample Accounting and Exclusions

- [ ] Add exact sample accounting for each phase.
  - Must include:
  - pilot-period participants
  - learning and recall sample
  - retention volunteers
  - any analysis-specific exclusions
- [ ] Resolve the mismatch between prose saying eight early trials and code/prose excluding participants `1001` through `1010`.
- [ ] Document the rationale for excluding participant `1063`.
- [ ] Document the rationale for any outlier removals used in primary analyses.
- [ ] Add or verify sensitivity checks for:
  - pilot exclusions
  - participant `1063`
  - H2b outlier removal

### Statistical Reporting and Interpretation

- [ ] Fix the inline demographics bug where the Education p-value appears to reuse the Lego variable.
  - Current target:
  - `_chaps/25-results.qmd:1300`
- [ ] Audit inline-reported statistics inserted from helper code or inline expressions.
- [ ] Correct the H3b ZINB interpretation so it remains on the multiplicative/log-link scale.
  - Current target:
  - `_chaps/25-results.qmd:4154-4165`
- [ ] Standardize outcome naming, especially `uncounted` versus `uncorrected` errors.

## P2: Evidentiary Discipline

- [ ] Reclassify H2b language from confirmatory acceptance to exploratory or sensitivity-supported evidence unless stronger support is demonstrated.
- [ ] Separate confirmatory findings from exploratory findings throughout Results and Conclusions.
- [ ] Reduce rhetorical overclaiming around retention and reliance effects.
- [ ] Clarify which outcomes are primary, secondary, and post hoc.
- [ ] Decide how the qualitative synthesis will be handled in `v1.1`.
  - Option A:
  - keep it and document the method transparently
  - Option B:
  - rewrite it as a clearly investigator-led thematic summary
  - Option C:
  - remove or substantially demote it in the public-facing dissertation if the method cannot be defended cleanly

## P3: Release Packaging

- [ ] Create a short `v1.1` release note describing what changed from the as-submitted dissertation.
- [ ] Make sure the published HTML version clearly identifies itself as `v1.1`.
- [ ] Add a visible link from the `v1.1` site to the as-submitted dissertation.
- [ ] Keep the as-submitted dissertation unchanged.
- [ ] Verify that repo docs only expose publication-safe material in the public-facing web path.

## Chapter Checklist

### Literature Review

- [ ] Remove visible placeholder theory text.
  - Current target:
  - `_chaps/22-lit_review.qmd:482`
- [ ] Fix visible image/table TODOs only where they affect the public HTML experience.

### Methods

- [ ] Remove TODOs and drafting residue.
- [ ] Fix terminology and copy defects identified in the review.
- [ ] Reconcile retention hypotheses and analysis descriptions with Results.
- [ ] Ensure the chapter describes what was actually done, not an obsolete plan.

### Results

- [ ] Remove visible warnings and placeholder text.
- [ ] Fix inline statistic/reporting bugs.
- [ ] Clean naming inconsistencies and copy defects.
- [ ] Tighten claim language for H2b and retention.
- [ ] Add explicit sample/exclusion accounting where needed for interpretation.

### Conclusions

- [ ] Tighten any conclusion that currently overstates H2b or retention.
- [ ] Fix visible copy defects.
- [ ] Align the conclusion language with the corrected Results framing.

### Appendices

- [ ] Remove or sanitize Appendix H for public release.
- [ ] Check whether any other appendix still contains operational notes, TODOs, or machine-specific details.

## Verification Steps

- [ ] Render the HTML build cleanly after each major correction batch.
- [ ] Search the active manuscript source for residual `TODO`, `subtitle...`, and similar placeholders.
- [ ] Search the rendered HTML for visible warning text and placeholder remnants.
- [ ] Compare `v1.1` against the as-submitted version to ensure the changes are corrective rather than expansive.
- [ ] Confirm that all known high-priority findings from the review are either fixed or explicitly deferred with justification.

## Definition of Done

`v1.1` is ready when:

- all `P0` items are complete
- all `P1` items are complete
- `P2` items have been addressed enough that the dissertation no longer overstates its evidence
- the HTML version is publication-safe and clearly marked as corrected
- the site links back to the as-submitted dissertation for transparency

## Explicit Deferrals

These items may remain outside `v1.1` unless they are needed to correct misleading content:

- extracting journal manuscripts
- major new analyses unrelated to identified errors
- broad restructuring of the dissertation narrative
- turning the repo into a full public reproducibility package

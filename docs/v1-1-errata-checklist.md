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

## P0: Publication Blockers [DONE]

- [X] Remove all visible TODOs, placeholders, and draft residue from active build chapters.
  - Current targets:
  - `_chaps/24-methods.qmd`
  - `_chaps/22-lit_review.qmd`
  - any appendix still included in the HTML build
- [X] Eliminate visible warnings or printed model diagnostics from rendered chapter output.
  - Known issue:
  - injected model warning in Results
- [X] Remove visible draft residue from Appendix H in publication-facing outputs.
  - Current target:
  - `_apps/38h-dataorg.qmd`
- [X] Remove visible placeholder text such as `subtitle...` from Results.
  - Current target:
  - `_chaps/25-results.qmd`
- [X] Fix the known publication-blocking copy defects identified in this `P0` pass.
  - Includes:
  - malformed words, repeated words, and obvious misspellings called out in the review

## P1: Internal Consistency and Correctness

### Methods and Results Reconciliation

- [X] Rewrite the Methods retention/hypothesis material so it matches the defended Results chapter in the H3 retention section.
  - Current targets:
  - `_chaps/24-methods.qmd:337-349`
  - `_chaps/24-methods.qmd:357-390`
  - `_chaps/24-methods.qmd:1587-1624`
- [X] Explain why OEE was abandoned for H3 and frame that change explicitly as a corrective Methods/Results reconciliation.
- [X] Review the rest of the Methods chapter for any remaining obsolete H3/OEE framing outside the corrected retention block.
- [X] Ensure hypothesis labels, outcome names, and analysis descriptions match across Methods, Results, and Conclusions.
  - Remaining H3b interpretive issues are documented through footnotes and Appendix F rather than by rewriting the defended narrative in place.

### Sample Accounting and Exclusions

- [X] Verify sample accounting and add targeted clarifications where needed for interpretation.
  - Completed work includes:
  - verification of pilot-period participants
  - verification of learning and recall samples
  - verification of retention volunteers
  - clarification of analysis-specific exclusions where they affect interpretation
- [X] Confirm that the eight-participant pilot exclusion is consistent with the defended data.
- [X] Document the rationale for excluding participant `1063`.
- [X] Document the rationale for primary-analysis outlier removals that materially affect interpretation.
- [X] Decide whether new sensitivity checks are required for `v1.1`.
  - Decision:
  - no new sensitivity checks were added in `v1.1` by design; see Appendix F `Intentional Deferrals`.

### Statistical Reporting and Interpretation

- [X] Fix the inline demographics bug where the Education p-value appears to reuse the Lego variable.
  - Current target:
  - `_chaps/25-results.qmd:1300`
- [X] Fix the exposed inline-reported statistic and labeling bugs identified in the review.
- [X] Document the H3b ZINB interpretation correction and its implications in Appendix F and cross-reference it from Results and Conclusions.
  - Current target:
  - `_chaps/25-results.qmd:4154-4165`
- [X] Standardize exposed outcome naming issues, especially `uncounted` versus `uncorrected` errors.

## P2: Evidentiary Discipline [DEFERRED BY DESIGN]

These items were reviewed and intentionally left outside the scope of `v1.1`, which is an errata, reconciliation, and publication-safety release rather than a broader revision:

- broader rhetorical tightening of `H2b` and retention claims
- confirmatory versus exploratory reframing beyond the specific corrections documented in Appendix F
- clarification of primary, secondary, and post hoc outcome status beyond what is already explicit in the defended manuscript
- broader revision of the qualitative-analysis method or its presentation

## P3: Release Packaging

- [X] Create a short `v1.1` release note describing what changed from the as-submitted dissertation.
- [X] Make sure the published HTML version clearly identifies itself as `v1.1`.
- [X] Add a visible link from the `v1.1` site to the as-submitted dissertation.
- [X] Keep the as-submitted dissertation unchanged.
- [X] Add a visible `v1.1` note to the corrected PDF title page.
- [ ] Add the GitHub compare/diff link to Appendix F once the final `v1.1` tag is published.
- [X] Verify that repo docs only expose publication-safe material in the public-facing web path.

## Chapter Checklist

### Literature Review

- [X] Remove visible placeholder theory text.
  - Current target:
  - `_chaps/22-lit_review.qmd:482`
- [X] Fix visible image/table TODOs only where they affect the public HTML experience.
  - No additional visible image/table TODOs were found in the public HTML path.

### Methods

- [X] Remove the visible TODO leak and rewrite the retention subsection as publication-safe prose.
- [X] Fix the Methods terminology and copy defects addressed in the `v1.1` pass.
- [X] Reconcile retention hypotheses and analysis descriptions with Results in the corrected H3 block.
- [X] Ensure the chapter describes what was actually done, not an obsolete plan.
  - Remaining legacy wording is now explicitly qualified by footnote rather than silently rewritten.

### Results

- [X] Remove visible warnings and placeholder text.
- [X] Fix inline statistic/reporting bugs.
- [X] Clean the exposed naming inconsistencies and copy defects addressed in the `v1.1` pass.
- [X] Decide whether broader H2b / retention language tightening belongs in `v1.1`.
  - Decision:
  - broader rhetorical tightening was deferred by design; see Appendix F `Intentional Deferrals`.
- [X] Add targeted sample/exclusion accounting where needed for interpretation.

### Conclusions

- [X] Decide whether broader conclusion tightening around H2b or retention belongs in `v1.1`.
  - Decision:
  - broader rhetorical tightening was deferred by design; see Appendix F `Intentional Deferrals`.
- [X] Fix visible copy defects.
- [X] Align the conclusion language with the corrected Results framing.
  - Alignment is achieved through the added footnote and Appendix F interpretation note rather than a quiet rewrite of the defended prose.

### Appendices

- [X] Remove visible draft residue from Appendix H for public release.
- [X] Add a direct link to the standalone defended IRB packet.
- [X] Decide whether deeper Appendix H softening belongs in `v1.1`.
  - Decision:
  - deeper appendix softening was deferred by design; see Appendix F `Intentional Deferrals`.
- [X] Check appendices in the public build path for visible operational notes, TODOs, or machine-specific details.

## Verification Steps

- [X] Render the HTML build cleanly after each major correction batch.
  - A pre-existing duplicate footnote-reference warning remains in the HTML acknowledgements render, but it does not appear to create a visible output defect in the published page.
- [X] Search the active manuscript source for residual `TODO`, `subtitle...`, and similar placeholders.
  - Residual source TODOs remain in non-public or intentionally deferred areas, but no new visible leaks remain in the public build path.
- [X] Search the rendered HTML for visible warning text and placeholder remnants.
- [X] Render the PDF build cleanly after the title-page and changelog updates.
- [X] Verify that the corrected PDF title page still fits on one page after adding the `v1.1` note.
- [X] Compare `v1.1` against the as-submitted version to ensure the changes are corrective rather than expansive.
  - Verified against the defended baseline for the active public-surface files touched by `v1.1`.
- [X] Confirm that all known high-priority findings from the review are either fixed or explicitly deferred with justification.

## Definition of Done

`v1.1` is ready when:

- all `P0` items are complete
- all `P1` items are complete
- `P2` items are either explicitly deferred by design or addressed through documented correction notes
- the HTML version is publication-safe and clearly marked as corrected
- the site links back to the as-submitted dissertation for transparency

## Explicit Deferrals

These items may remain outside `v1.1` unless they are needed to correct misleading content:

- extracting journal manuscripts
- major new analyses unrelated to identified errors
- broad restructuring of the dissertation narrative
- turning the repo into a full public reproducibility package
- broader rhetorical tightening around `H2b` and retention beyond the specific documented corrections
- new sensitivity analyses or robustness checks
- broader qualitative-method revision
- deeper appendix softening beyond visible public-facing issues
- full inline-stat auditing beyond the specific exposed bugs corrected in `v1.1`

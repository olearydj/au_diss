**Initial Findings**
This repo already contains a defensible final artifact set, but it is not yet a clean archival baseline.

- The dissertation source is centered on Quarto book config in [_quarto.yml](/Volumes/Casa/dev/dissertation/_quarto.yml), with a rendered 304-page PDF in [manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf](/Volumes/Casa/dev/dissertation/manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf) and an archived defended snapshot in [defended-2024-08-02](/Volumes/Casa/dev/dissertation/defended-2024-08-02).
- The worktree is currently mixed: defended manuscript source, later revision edits, untracked analysis artifacts, generated HTML/figure outputs, and exploratory modeling notebooks all live together.
- The repo has no top-level project documentation, so the build path, data provenance, and intended file layout are implicit rather than stated.
- The analysis pipeline is only partly automated. Quarto/R is the main path, but some data generation depends on manual video processing/annotation plus Python utilities with hard-coded local paths.
- There are still draft markers, TODOs, and issue notes in source files, even though the dissertation itself is complete.
- Quarto is available locally, but in this shell `Rscript` was not on `PATH`, so I have not yet verified a clean rebuild from source.

**Current Working Decisions**
- The baseline reproducibility target starts at `Level 1`: a content-identical build with matching manuscript text, analysis outputs, pagination, figures, and tables.
- `Level 2` byte-identical output is deferred unless it becomes straightforward after the `Level 1` build is stable.
- Baseline work is being isolated on branch `safety-2026-03-11-pre-baseline` rather than on `master`.
- The current focus is still Steps 2 and 3: define the rebuild target and verify a defended-quality rebuild before cleanup or archival commits.

**Current Baseline Interpretation**
- Canonical manuscript artifact:
  [defended-2024-08-02/main.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf)
- Canonical deposited package artifact:
  [defended-2024-08-02/oleary-2024-08-02.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/oleary-2024-08-02.pdf)
- Canonical IRB appendix packet:
  [defended-2024-08-02/irb.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/irb.pdf)
- Current source is treated as the effective archival source, with three documented deltas from the canonical manuscript artifact:
  - Acknowledgements wording in [_front/13-acknowledgements.qmd](/Volumes/Casa/dev/dissertation/_front/13-acknowledgements.qmd)
  - rebuilt-only `compare_performance(...)` warning injected into Results during current rendering
  - missing `January` in one reference entry during current bibliography rendering
- Current build/provenance understanding is:
  1. render the Quarto book
  2. historically post-process the resulting manuscript PDF to correct the front-matter / empty-chapter artifact
  3. combine the corrected manuscript PDF with the separately produced IRB packet to create the deposited package

**Agreed Next Sequence**
This is the working order to follow from this point, and should be treated as the paper trail if later cleanup goes sideways.

1. Documentation and baseline definition first.
Deliverables:
`README.md`, `docs/build.md`, `docs/artifacts.md`, and minimal `.gitignore` cleanup.
Goals:
- define the canonical artifacts
- define the canonical source state and the three documented deltas from `main.pdf`
- record the build/provenance note permanently
- avoid aggressive cleanup while environment evidence is still being captured

2. Capture the current reproducible environment without overwriting historical intent.
Goals:
- capture the current R environment as a new lockfile and/or manifest, not an in-place replacement of `renv.lock`
- turn on `keep-tex: true`
- do one more successful render
- preserve and harvest `.tex`, `.log`, and `.fls` if produced
- derive the actual LaTeX package footprint used by the successful build

3. Make the environment decision after evidence is captured.
Goal:
- decide whether the new R lockfile should become canonical baseline support material or remain a reproducibility snapshot distinct from the historical `renv.lock`

4. Only then do final cleanup, baseline commit, and tag.
Goals:
- perform generated-noise triage
- finalize `.gitignore`
- commit on `safety-2026-03-11-pre-baseline`
- tag the archival baseline

**Recommended Plan**
1. Create a safety snapshot of the current repo state.
This is not the real baseline. It is just protection before cleanup or rebuild work begins.
Deliverable: a temporary branch or checkpoint commit preserving the exact current worktree.

2. Define what “identical results” means for the baseline.
I recommend two levels:
Level 1: content-identical build, meaning same analysis outputs, pagination, figures, tables, and manuscript text.
Level 2: byte-identical artifact, which is stricter and may require controlling PDF metadata, timestamps, `date: today`, package versions, fonts, and TeX behavior.
Deliverable: an explicit reproducibility target before we start debugging the build.

3. Reconstruct and verify the defended build path before any cleanup.
This is the gating step for the real baseline.
Work includes identifying the exact render command/profile, verifying Quarto/R/renv/TeX dependencies, restoring any missing environment pieces, and rendering the dissertation from a clean checkout.
We should compare the fresh output against the defended PDF and the August 2, 2024 snapshot using `pdfinfo`, page counts, extracted text, figure/table spot checks, and if needed PDF diff tooling.
Deliverable: a documented build procedure and a verified rebuild result.

4. Resolve sources of non-determinism until the build is stable enough to baseline.
Likely candidates are `date: today` in [_quarto.yml](/Volumes/Casa/dev/dissertation/_quarto.yml), package drift, random seeds in analysis code, font/LaTeX differences, and generated metadata in PDFs.
Deliverable: a stable build process with known constraints and any necessary pinning documented.

5. Classify the repository contents into canonical, archival, generated, exploratory, and ignored.
Right now those categories are blended together.
Canonical should likely include manuscript source, templates, curated data needed to rebuild results, core scripts, and final defended outputs.
Generated and local-noise content should likely be removed from version control or ignored.
Exploratory notebooks like [25-h1b-nonlinear.qmd](/Volumes/Casa/dev/dissertation/25-h1b-nonlinear.qmd), [25-linear-pw.qmd](/Volumes/Casa/dev/dissertation/25-linear-pw.qmd), [h1b_mod_select.qmd](/Volumes/Casa/dev/dissertation/h1b_mod_select.qmd), and [_chaps/25-m7r.qmd](/Volumes/Casa/dev/dissertation/_chaps/25-m7r.qmd) should either move to an archive/exploratory area or be removed from the canonical baseline.
Deliverable: a keep/archive/ignore decision list and updated `.gitignore`.

6. Clean the source tree without altering the defended content.
The goal here is not to rewrite the dissertation. It is to remove repository noise and move working notes out of the canonical source.
Targets include draft issue files like [00-issues.md](/Volumes/Casa/dev/dissertation/archive/00-issues.md), machine-specific notes in [_apps/38h-dataorg.qmd](/Volumes/Casa/dev/dissertation/_apps/38h-dataorg.qmd), unneeded generated HTML/figure folders, `.DS_Store`, workspace files, and inline draft markers that should live in docs instead of manuscript source.
Deliverable: a cleaner source tree that still reproduces the defended work.

7. Add proper repository documentation.
At minimum I recommend:
`README.md`: project overview, repo layout, build instructions, authoritative outputs.
`docs/build.md`: exact reproduction workflow and environment requirements.
`docs/reproducibility.md`: what is fully reproducible, what is manual, what is private.
`docs/data.md`: data inventory, provenance, privacy boundaries, and how `combined_results.xlsx` was produced.
`docs/repo-map.md`: quick explanation of `_chaps`, `_apps`, `data`, `rdata`, `parse_xml`, `tex`, `manuscript`, `defended-2024-08-02`.
`docs/publications.md`: map dissertation chapters/results to planned follow-on papers.
Deliverable: a repo that a future you can understand in minutes instead of re-discovering over days.

8. Make the helper scripts portable enough for publication work.
The Python utilities currently assume specific local storage and Box paths. Those should be parameterized through env vars or a small config file.
I would also add thin wrapper scripts for common actions like rendering the full book and selected chapters.
Deliverable: scripts that work off documented config instead of one machine layout.

9. Establish the real archival baseline.
Only after the build is verified and the repo is cleaned/documented.
Deliverable: one clean commit plus an annotated tag representing the defended dissertation baseline.

10. Start publication development from branches off that baseline.
The dissertation repo should become a stable source-of-truth archive. New papers should be developed in branches or sibling repos derived from that baseline, not by continuing to mutate the archival branch.
Deliverable: a clear branching strategy for publications.

**Suggested Working Order**
I’d do this in the following sequence:

1. Safety snapshot.
2. Define reproducibility target.
3. Verify clean rebuild of the defended dissertation.
4. Documentation and baseline definition.
5. Capture R and TeX environment evidence.
6. Decide how to represent the captured environment in-repo.
7. Curate repo contents and `.gitignore`.
8. Clean manuscript-adjacent residue.
9. Refactor path-dependent scripts.
10. Create baseline commit and tag.
11. Open publication branches.

**What I’d Start With**
The first concrete step should be Step 2 and Step 3 together: define the rebuild target, then prove we can render the dissertation with matching results before touching cleanup.

If you want, the next turn I can turn Step 2 into a precise rebuild-verification checklist and then start Step 3 by inventorying the exact commands, profiles, and environment assumptions needed to render the defended book.

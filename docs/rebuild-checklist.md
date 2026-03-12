**Rebuild Checklist**
This document turns Steps 2 and 3 of [baseline-plan.md](/Volumes/Casa/dev/dissertation/docs/baseline-plan.md) into a concrete verification workflow.

**Current Decision**
- Baseline target: `Level 1` content-identical build.
- Stretch target: `Level 2` byte-identical PDF only if it is low-friction after `Level 1` is achieved.

**Level 1 Acceptance Criteria**
A rebuild is considered acceptable for baseline purposes if all of the following are true:

- The dissertation renders successfully from source to PDF.
- The rebuilt PDF has the same chapter and appendix set as the defended dissertation.
- The rebuilt PDF has the same pagination and page count as the defended dissertation, unless a specific and justified build difference is documented.
- Figures, tables, captions, and major layout features appear in the same places and with the same content.
- Key quantitative results in the abstract, results, conclusions, and major summary tables match the defended dissertation.
- Differences in PDF metadata, timestamps, producer strings, or raw file hash are allowed at this stage.

**Authoritative Reference Artifacts**
These are the reference points the rebuild should be checked against:

- Defended manuscript PDF:
  [manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf](/Volumes/Casa/dev/dissertation/manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf)
- Archived defended/deposit snapshot:
  [defended-2024-08-02/oleary-2024-08-02.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/oleary-2024-08-02.pdf)
- Main Quarto configuration under review:
  [_quarto.yml](/Volumes/Casa/dev/dissertation/_quarto.yml)

Important distinction:

- The defended/local manuscript artifact is a `304`-page dissertation PDF.
- The archived submission/deposit artifact is a `427`-page package that includes appended IRB materials beginning after the dissertation body.
- A downloaded Auburn repository copy was checked and matches the `427`-page submission/deposit artifact class, not the `304`-page manuscript artifact.
- The repo contains the likely exact source components of that deposited package:
  [main.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf) (`304` pages) and
  [irb.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/irb.pdf) (`123` pages), which sum to `427` pages.

**Immediate Environment Findings**
Current shell findings:

- `quarto` is available on `PATH`
- `pdflatex` and `xelatex` are available on `PATH`
- `R` is not available on `PATH`
- `Rscript` is not available on `PATH`
- `latexmk` is not available on `PATH`

These findings do not prove the project cannot build on this machine, but they do mean the first technical task is to locate or restore the intended R runtime for this workspace.

Update on current machine:

- `R` is now installed and available at `/usr/local/bin/R`
- `Rscript` is now installed and available at `/usr/local/bin/Rscript`
- Installed version: `R 4.4.0 (2024-04-24)`
- Platform: `aarch64-apple-darwin20`

Interpretation:

- The current machine now matches the R major/minor version pinned in [renv.lock](/Volumes/Casa/dev/dissertation/renv.lock).
- This materially reduces one major source of environment drift before the first rebuild attempt.
- Quarto and TeX were already available on the current machine before R was installed.

**Prior Machine Findings**
The prior machine currently reports:

- `R`: `/usr/local/bin/R`
- `Rscript`: `/usr/local/bin/Rscript`
- `R version 4.4.3 (2025-02-28)`
- `quarto 1.6.43`
- `pdfTeX 3.141592653-2.6-1.40.27 (TeX Live 2025)`
- `XeTeX 3.141592653-2.6-0.999997 (TeX Live 2025)`

Interpretation:

- The prior machine does have a usable R installation.
- That installation is newer than the defended dissertation build date of August 2, 2024.
- Therefore, the prior machine is useful for reconstructing the current build path and installation method, but it should not be assumed to represent the exact defended environment.
- Matching the defended dissertation at `Level 1` may still be possible from this newer environment, but any discrepancies will need to be evaluated as potential environment drift.

**Current Rebuild State**
As of this checkpoint:

- `R 4.4.0` is installed on the current machine and available on `PATH`.
- The current-platform `renv` library at `renv/library/macos/R-4.4/aarch64-apple-darwin20` was deleted and rebuilt from scratch.
- `renv::restore(prompt = FALSE)` completed successfully for the lockfile-defined environment.
- The most useful historical package evidence is now documented in:
  [intel-renv-manifest.md](/Volumes/Casa/dev/dissertation/docs/intel-renv-manifest.md)
- TeX-side and PDF-engine dependencies discovered during rebuild are tracked in:
  [tex-dependencies.md](/Volumes/Casa/dev/dissertation/docs/tex-dependencies.md)
- The current successful-build R snapshot is documented in:
  [r-environment-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/r-environment-2026-03-12.md)
- The actual LaTeX package footprint extracted from the successful build artifacts is documented in:
  [tex-package-footprint-2026-03-12.md](/Volumes/Casa/dev/dissertation/docs/tex-package-footprint-2026-03-12.md)
- Content-only PDF comparison findings are documented in:
  [text-content-diff.md](/Volumes/Casa/dev/dissertation/docs/text-content-diff.md)
- The preserved Intel library is only partly readable locally because most entries are broken symlinks into the old `renv` cache, but those symlink targets still preserve many exact package versions.
- A frozen Posit Package Manager snapshot dated `2024-08-02` was used to rebuild the arm64 project library for the first serious render attempt.
- `renv::status()` remains noisy and is not currently a clean gating signal, because it scans the whole repo and the lockfile does not fully cover the present source tree.
- Temporary local comparison copies and pre-render backups were created during rebuild investigation to protect existing outputs and compare the direct render against `main.pdf`.
- A fresh empty render target was created at:
  [manuscript](/Volumes/Casa/dev/dissertation/manuscript)
- The dissertation now renders successfully to PDF on the current machine at:
  [manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf](/Volumes/Casa/dev/dissertation/manuscript/Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.pdf)
- The render still reproduces a known historical front-matter artifact: an extra first `Abstract` page appears before the title page in the direct Quarto PDF output.
- Based on source inspection and author confirmation, the defended dissertation was produced by rendering with that extra first page and then deleting that page from the PDF afterward.
- Content-only comparison found one rebuilt-only Results artifact caused by runtime output from `compare_performance(...)` being emitted into the document stream. In the generated TeX this appears as:
  `Random effect variances not available. Returned R2 does not account for random effects.`
  immediately before the model-performance table. This is a build artifact from the current package stack, not dissertation prose.
- Comparison against the archived `427`-page submission artifact shows that it is not simply the same PDF with different metadata. It is a larger deposited package with appended IRB material beginning at page `305`.
- The deposited artifact appears to have been assembled after the manuscript render by appending at least the IRB packet PDF to the manuscript PDF.
- The Quarto project also defines an HTML output path.
- That HTML path has now been re-verified successfully on the current machine with:
  `quarto render --to html --output-dir html`
- The regenerated `html/` tree includes the active chapter and appendix set from `_quarto.yml` and produces the expected `_chaps/`, `_apps/`, `images/`, `css/`, `site_libs/`, and `search.json` artifacts.
- The previously stale extra pages in the historical `html/` tree
  (`_chaps/27-colophon.html`, `_apps/33c-s1conduct.html`, `_apps/34d-s2conduct.html`, and `_apps/37g-datadict.html`)
  are no longer present after regeneration.
- `downlit` was subsequently installed into the project library, and a follow-up HTML render completed without the prior code-link warning.
- `css/custom.css` was also updated to override the newer Bootstrap inline-code background so the rebuilt HTML matches the older light inline-code pill appearance in the archived `html/` output.
- A separate current-build R lock snapshot was captured at:
  [renv-baseline-2026-03-12.lock](/Volumes/Casa/dev/dissertation/docs/renv-baseline-2026-03-12.lock)
  with supporting artifacts:
  [r-package-manifest-2026-03-12.csv](/Volumes/Casa/dev/dissertation/docs/r-package-manifest-2026-03-12.csv)
  and
  [r-session-info-2026-03-12.txt](/Volumes/Casa/dev/dissertation/docs/r-session-info-2026-03-12.txt)
- That alternate lock snapshot should currently be treated as a verified current-build environment capture, not as a proven historical replacement for the top-level `renv.lock`.
- The successful TeX render footprint was extracted from generated `.tex`, `.fls`, and `.log` artifacts during the rebuild process; those artifacts were later dropped after the findings were documented.
- The data workflow is also now better understood:
  - `data/combined_results.xlsx` is the curated main-study workbook from the original aggregation path
  - retention/H3 data was not folded back into that export path
  - `data/source/i1_h3.xlsx` is a separate support workbook used directly by the H3 analysis
  - this split is consistent with the surviving `forms_data.Rmd` TODO to "add phase 3" and with author confirmation that H3 was analyzed later in a more ad hoc workflow

Interpretation:

- The current machine can now execute the full Quarto/R/LaTeX/Biber pipeline.
- The current machine can also execute the HTML/book render path cleanly, with working code-link support and inline-code styling aligned more closely with the archived HTML output.
- The remaining baseline question is no longer “can it build?” but which artifact should be treated as the primary baseline target:
  the `304`-page manuscript or the `427`-page deposited package.
- The build procedure therefore includes at least one documented manual post-processing step unless a source-side fix is adopted later on a non-baseline branch.

**Current Baseline Rule**
For current baselining work, interpret the repository and artifacts as follows:

- The canonical manuscript artifact is:
  [defended-2024-08-02/main.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/main.pdf)
- The canonical deposited package artifact is:
  [defended-2024-08-02/oleary-2024-08-02.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/oleary-2024-08-02.pdf)
- The IRB packet used for deposit assembly is:
  [defended-2024-08-02/irb.pdf](/Volumes/Casa/dev/dissertation/defended-2024-08-02/irb.pdf)
- The current source tree is treated as the effective archival source, with only three documented text-level deltas from the canonical manuscript artifact:
  - Acknowledgements wording
  - rebuilt-only `compare_performance(...)` warning emitted into Results
  - missing `January` in one reference during current bibliography rendering

**Agreed Work Sequence**
This is the agreed execution order from this point forward:

1. Documentation first.
Create and/or finalize:
- `README.md`
- `docs/build.md`
- `docs/artifacts.md`
- minimal `.gitignore` cleanup

2. Capture environment evidence before aggressive cleanup.
Do not rewrite `renv.lock` in place yet.
Do:
- capture the current R environment as a new lockfile and/or manifest
- enable `keep-tex: true`
- perform one more successful render
- preserve `.tex`, `.log`, and `.fls` if available
- extract the actual LaTeX package footprint used by the successful build

3. Decide how to represent the captured environment.
Only after the evidence exists should we decide whether a new R lockfile becomes canonical support material or remains a separate reproducibility snapshot.

4. Final cleanup and archival baseline work.
Only after documentation and environment capture:
- perform generated-noise triage
- finalize `.gitignore`
- commit on `safety-2026-03-11-pre-baseline`
- tag the archival baseline

**Verification Workflow**
1. Confirm the authoritative build target.
Decide which artifact is the primary comparison source: the defended manuscript PDF in `manuscript/`, the archived August 2, 2024 submission PDF, or both.

2. Capture fingerprints from the authoritative PDF.
Record page count, title, author, creation date, chapter list, appendix list, and a short list of spot-check pages, tables, and figures that must match.

3. Confirm the authoritative render path.
Determine which Quarto configuration and command were actually used to produce the defended dissertation. The repo currently contains multiple Quarto config variants, so this must be resolved explicitly.

4. Restore the build environment.
Find the intended R installation and confirm `renv` and required system dependencies are available. If needed, document PATH fixes or wrapper commands.

5. Perform a clean render attempt.
Run the dissertation build from source without modifying manuscript content. Record the exact command used and where output is written.

6. Apply any known historical post-processing steps.
At present, the known required step is removal of the extra first `Abstract` page from the direct Quarto-rendered PDF.

7. Compare rebuilt output to the reference artifact.
Check:
- page count
- chapter and appendix order
- title page and front matter
- abstract text
- selected results tables and summary statements
- selected figures and captions
- conclusions summary

8. Log every discrepancy.
For each mismatch, classify it as one of:
- environment drift
- config ambiguity
- source drift since the defended build
- generated-artifact noise
- unknown

9. Resolve only build/reproducibility issues.
Do not start general cleanup until the build target is met or the remaining gaps are understood and documented.

10. Freeze the verified build procedure.
Once the rebuild is acceptable, capture the exact workflow in a permanent build document.

**Open Questions To Resolve During Rebuild**
- Which Quarto config path is authoritative for the defended PDF?
- Is the current `_quarto.yml` already the defended config, or was it swapped in manually from another variant?
- Is the `date: today` field materially affecting front matter or PDF metadata?
- Are the current manuscript source edits post-defense refinements that must be excluded from the real baseline?
- Are any untracked data or `rdata/` files required to reproduce the defended PDF exactly at the content level?
- Does the HTML/website render path in `_quarto.yml` need any further cleanup beyond deciding whether to keep the inline-code compatibility override?

**Next Action**
The immediate next tasks are:

1. Decide whether the alternate R lock snapshot remains documentary support material or should be promoted later.
2. Decide whether the updated alternate R environment capture should remain documentary support material or be promoted later.
3. Continue with broader generated-noise cleanup before the baseline commit.

# Dissertation v1.1.1 Pre-Release Review

## Executive summary

**Overall soundness verdict: the substantive record is sound.** Across all 37 adversarially-verified findings, none changes a hypothesis decision, a fitted estimate, a test statistic, a p-value, or an effect-size point estimate. Every confirmed defect is a reporting, consistency, interpretive, or editorial slip that is conclusion-neutral. The accepted/rejected status of H1a–H3b is unaffected.

**One finding reaches the "real defect" bar set by the already-handled bootstrap reseed bug:** F-003 (H2b reliance summary states wrong magnitudes *and* an inverted direction versus its own bootstrap table, and the inverted direction propagates into the Conclusions chapter). Four more reader-facing numeric/consistency/editorial errors are close behind (F-004, F-015, F-019, F-022).

**Confirmed errata by severity (25 errata-eligible findings):**

| Severity | Count | Findings |
|---|---|---|
| High | 1 | F-003 |
| Medium | 5 | F-004, F-008, F-015, F-019, F-022 |
| Low | 19 | F-001, F-005, F-009, F-013, F-016, F-017, F-018, F-020, F-023, F-025, F-026, F-027, F-028, F-029, F-030, F-031, F-032, F-034, F-035 |

(Of the Low tier, F-026–F-032 are seven copy/grammar findings covering roughly a dozen individual repeated-word, misspelling, and verb-form slips.)

**One-line recommendation:** Fold the five reader-facing numeric/consistency errors into v1.1.1 as footnotes + Appendix F entries (F-003 is the mandatory one), batch-fix the render/copy defects inline in the web build per the v1.1 P0 precedent, defer the remaining low-severity items to a later pass — the release is otherwise clear to ship.

---

## Part 1 — Errata-eligible findings (ranked by severity)

### HIGH

#### [DONE] F-003 — H2b reliance summary states wrong magnitudes AND inverted direction vs its own bootstrap table
- **Location:** `_chaps/25-results.qmd:3660` (rendered `manuscript/dissertation.tex:10678`); summarizes `tbl-boot-pwi` (`:3651–3658`). Propagates to `_chaps/26-conclusions.qmd` lines 34, 38, 89 (tex `:12400`).
- **Issue:** Prose claims "AR and MR reduce reliance by 0.686 and 0.612 seconds per reference … relative to PWI" and "reduce reliance more than PAR and PWI." Both the magnitudes and the direction are wrong.
- **Evidence:** Recomputed from `rdata/h2b_pwi_boot_res.RData` (matches rendered table): PWI−AR = −0.993 (HL −1.064), PWI−MR = −0.880 (HL −0.956); all PWI-minus-treatment differences are negative, so PWI has the *lowest* time-per-reference composite (group means PWI 0.36 < MR 1.24 < AR 1.35, z>2.5, n=48). AR/MR therefore *increase* time per reference relative to PWI. The figures 0.686/0.612 occur exactly once each in the whole rendered tex and appear nowhere in the reliance table — a carryover from the H2a OEE discussion. The v1.1 changelog (`_apps/39i-v1-1-changelog.qmd:15`) shows this sentence was edited in v1.1 (a "FIX THIS" marker removed) without fixing the figures.
- **Errata class:** consistency (factual reporting error). **Severity:** High. **Accept-H2b is unchanged.**
- **Disposition:** **Fold into v1.1.1 now (footnote + Appendix F).** This is the one finding that clearly meets the bootstrap-seed-bug bar.
- **Suggested correction (footnote at `:3660` + Appendix F row):**
  > Erratum (v1.1.1): As reported, this sentence misstated both the magnitude and the direction of the pairwise reliance differences. Per @tbl-boot-pwi the signed bootstrap differences are PWI − AR = −0.993 and PWI − MR = −0.880 on the mean (−1.064 and −0.956 on the Hodges–Lehmann estimator). Because the differences are signed PWI-minus-treatment and are negative, PWI shows the *lowest* reliance composite; AR and MR exhibit *higher*, not lower, time per reference than PWI on this measure. The values 0.686 and 0.612 were carried over in error from the H2a OEE discussion and do not appear in this table. The accept-H2b determination is unchanged, and the Results caution that specific pairwise differences are not clear enough to declare continues to govern. The Conclusions phrasings "AR and MR tend to reduce reliance more than PAR and PWI" and "reduced reliance on instructions for AR and MR users" (`26-conclusions.qmd` lines 34, 38, 89) should be read subject to this correction.

---

### MEDIUM

#### [DONE] F-022 — Malformed citation: missing `@` sigil prints a raw BibTeX key in the text
- **Location:** `_chaps/22-lit_review.qmd:807` (rendered `manuscript/dissertation.tex:3937`, `html/_chaps/22-lit_review.html:1349`, `html/search.json:177`).
- **Issue:** In `[@palmarini2017innov; @borsci2015empir; danielsson2020augme]` the third key lacks its `@`. Pandoc does not resolve it, so the raw string "danielsson2020augme]" prints as literal body text in both PDF and HTML. The same key resolves correctly at lines 789 and 811, confirming an accidental dropped sigil.
- **Errata class:** editorial (reader-visible render defect on a load-bearing citation). **Severity:** Medium.
- **Disposition:** **Fold into v1.1.1: inline source fix in the web build + Appendix F roll-up row.**
- **Suggested correction:** change to `[@palmarini2017innov; @borsci2015empir; @danielsson2020augme]` so it renders "(Palmarini et al., 2017; Borsci et al., 2015; Danielsson et al., 2020)." Appendix F row: "Literature Review, Needs and Recommendations | A malformed inline citation omitted the '@' on the third key, so the raw BibTeX key printed as literal text in PDF and HTML | Restored the missing '@' so the citation resolves to Danielsson et al. (2020) | Corrects a reader-visible rendering defect without changing the cited sources or the argument."

#### [PENDING] F-019 — Empirical-contribution claim misattributes high error rates to PAR, contradicting H1c
- **Location:** `_chaps/26-conclusions.qmd:154` (rendered tex `:12875`).
- **Issue:** "PWI and PAR demonstrated faster initial performance but higher error rates" contradicts the dissertation's own H1c result, which placed PAR on the accurate side.
- **Evidence:** H1c (`25-results.qmd:2831`): PWI differs from all others; "PAR, AR, and MR treatments are statistically similar." Conclusions summary (`26-conclusions.qmd:21`): "All augmented instruction methods (PAR, AR, MR) result in significantly lower error rates compared to PWI." Observed mean UCE: PWI 6.14, PAR 0.76, AR 0.64, MR 0.52 — PAR is ~8× below PWI. PAR was fast (H1a) AND low-error (H1c), so it does not exhibit the asserted trade-off.
- **Errata class:** consistency. **Severity:** Medium. Decisions unchanged.
- **Disposition:** **Fold into v1.1.1 (footnote + Appendix F).**
- **Suggested correction (footnote at `:154`):**
  > Erratum (v1.1.1): The Empirical Contributions summary groups PAR with PWI as "faster initial performance but higher error rates." This is inconsistent with the defended H1c result and the data: PAR's uncorrected error count was significantly lower than PWI and statistically indistinguishable from AR and MR (see H1c and @tbl-learn-results-summary). PAR was both fast (H1a) and low-error (H1c) and therefore does not exhibit the speed-accuracy trade-off described here. The trade-off should be read as between PWI (fast, error-prone) and the immersive AR/MR methods (slower, significantly more accurate), with PAR as the favorable exception combining speed with low error. The estimates, tests, and hypothesis decisions are unchanged.

#### [DONE] F-015 — H1b summary says "controlling for iTCT" but the analysis controls for initial TCT ($TCT_0$)
- **Location:** `_chaps/26-conclusions.qmd:20`, H1b row of `tbl-learn-results-summary` (rendered tex `:12333`).
- **Issue:** "iTCT" is defined throughout as a retention-phase quantity (the *increase* in TCT, `25-results.qmd:3808`), a variable that does not exist in the learning phase. The H1b model controls for each participant's *initial* TCT (`initial_tct = first(tct)`, `:2350`; "holding $TCT_0$ constant," `:2641`; "controlling for initial task completion time," `:2708`). Applying the retention acronym to a learning-phase covariate is internally contradictory.
- **Errata class:** consistency (outcome-variable naming). **Severity:** Medium.
- **Disposition:** **Fold into v1.1.1: inline fix + Appendix F row.**
- **Suggested correction:** replace "when controlling for iTCT" with "when controlling for initial TCT ($TCT_0$)". Appendix F: "Conclusions, H1b summary table | the key-findings cell applied the retention-phase variable name iTCT to the learning-phase covariate | Corrected to 'controlling for initial TCT ($TCT_0$)' to match the Results description (holding $TCT_0$ constant) | Fixes an outcome-variable labeling inconsistency; the analysis and ranking are unchanged."

#### [PENDING] F-004 — Reported PWI–MR OEE difference (0.307) is exactly half the correct value (~0.614)
- **Location:** `_chaps/25-results.qmd:3262` (rendered tex `:10453`), prose after `tbl-boot-oee`.
- **Issue:** "average estimated differences of 0.687 (PAR), 0.585 (AR), and 0.307 (MR)." The rule (mean of absolute Mean/Median/HL differences) reproduces PAR (0.687) and AR (0.585) *exactly*, confirming the method, but PWI–MR computes to 0.614 from `rdata/h2a_oee_boot_res.RData` (Mean −0.448, Median −0.729, HL −0.664). The printed 0.307 = 0.6138/2 — a halving/transcription slip. No alternative computation yields 0.307.
- **Errata class:** consistency. **Severity:** Medium (prosecutor)/Low (defender) → reported as Medium because it is a wrong printed number. Accept-H2a unchanged (MR still smaller than PAR either way).
- **Disposition:** **Fold into v1.1.1 (footnote, value left in place per policy).**
- **Suggested correction (footnote at `:3262`):**
  > Erratum (v1.1.1): the PWI–MR average estimated difference was misprinted as 0.307; the value computed from the cached bootstrap artifact (mean of the absolute Mean, Median, and Hodges–Lehmann differences) is 0.614. The PWI–PAR (0.687) and PWI–AR (0.585) values are correct. The H2a conclusion is unchanged.

#### [DEFERRED] F-008 — Poisson model-comparison prose claims the interaction model is better on BIC, but its own table shows the opposite
- **Location:** `_chaps/25-results.qmd:4086`, table `tbl-uce-modperf-pm` (tex `:11126–11127`).
- **Issue:** Text says the interaction model "performs better on AIC, BIC, and RMSE." The table shows it is better on AIC (223.9 vs 226.6) and RMSE but *worse* on BIC (233.3 vs 232.5), with the BIC weight favoring the additive model (0.61 vs 0.39). AIC/RMSE/equal-R² claims are correct; only the BIC claim is false.
- **Errata class:** consistency. **Severity:** Medium. No downstream impact — both Poisson models are discarded one paragraph later (`:4104`) for overdispersion in favor of NB/ZINB.
- **Disposition:** **Defer to a later errata pass** (inert, discarded branch), or fold a short footnote if convenient.
- **Suggested correction (footnote at `:4086`):**
  > As displayed in @tbl-uce-modperf-pm, the interaction Poisson model is better on AIC and RMSE but not on BIC; the additive model has the lower BIC (232.5 vs 233.3) and the larger BIC weight (0.61 vs 0.39). The sentence should read that the interaction model is favored on AIC and RMSE while BIC marginally favors the additive specification. This does not affect model selection: both Poisson models are subsequently discarded for overdispersion in favor of the NB/ZINB models.

---

### LOW

#### [DEFERRED] F-001 — "-0.75 correlation between log term and intercept" cited for a participant-level reading is the fixed-effect (sampling) correlation, not the random-effect correlation
- **Location:** `_chaps/25-results.qmd:2284` (H1b, model m7).
- **Issue:** −0.75 is `cov2cor(vcov(m7))[Intercept, log] = −0.749` — lme4's "Correlation of Fixed Effects," a property of the estimator's sampling covariance / design collinearity. The stated participant-level reading ("participants with higher initial TCT experience a stronger log-term effect … power law of practice") corresponds to the *random-effect* correlation `VarCorr(m7)` cor(intercept, log slope) = −0.849 (rounds to −0.85). Same sign and comparable magnitude, so the qualitative conclusion is corroborated, not lucky.
- **Errata class:** interpretive. **Severity:** Low. Nothing in model selection or estimates changes.
- **Disposition:** **Disclose-only / optional footnote.**
- **Suggested correction (footnote):** note that −0.75 is the fixed-effect estimate correlation (design collinearity), while the participant-level reading is carried by the random-effect correlation −0.85; both are strongly negative and the conclusion is unchanged.

#### [DONE] F-005 — Reliance histogram subtitle says "left-skewed"; the distribution is strongly right-skewed
- **Location:** `_chaps/25-results.qmd:3351`, `fig-pwi-hist` subtitle.
- **Issue:** `pwi_time_per_ref_agg` has a zero spike (22/53 = 0), a long upper tail to 5.45, and sample skewness ≈ +1.49 — textbook positive/right skew. Contradicts the chapter's own body text at `:3325` (components "strongly right-skewed," skewness 4.51 and 5.64). No reading makes a zero-spike-plus-long-upper-tail "left-skewed."
- **Errata class:** editorial (sign error in a decorative subtitle). **Severity:** Low. No analysis depends on it.
- **Disposition:** **Fix inline in web build** (single word): "left-skewed" → "right-skewed" + Appendix F roll-up.

#### [DONE] F-023 — Affordance referenced as "Egocentric Display" but the framework defines it as "User-Centric Display"
- **Location:** `_chaps/22-lit_review.qmd:860` vs `tbl-afford` item #9 (`:847`); the canonical name is used at `24-methods.qmd:196/673/1580`, `23-prob_statement.qmd:28`, `26-conclusions.qmd:105/126`, and the very next paragraph `22-lit_review.qmd:862`.
- **Issue:** "Egocentric Display" appears exactly once in the corpus and is not a defined affordance; the quotation marks and parallel construction signal it is meant to name affordance #9.
- **Errata class:** consistency/editorial. **Severity:** Low. No analysis affected.
- **Disposition:** **Fix inline in web build** (one word): "Egocentric Display" → "User-Centric Display" + Appendix F roll-up.

#### [PENDING] F-013 — H3b "Adj Coef" halving misapplied to scale-invariant rate ratios (PWI factor stated as 0.197; rate ratio is 0.394)
- **Location:** `_chaps/25-results.qmd` chunk `tbl-uce-modsum` (`:4149–4158`), body `:4166`, equation `eq:m3-uce-pwi` (`:4173–4174`).
- **Issue:** The "Adj Coef" column divides every exponentiated coefficient by 2 to reverse the 2× iUCE rescaling. That division is valid only for the intercept (an expected count: 6.709/2 = 3.354). The treatment/gap exponentiated coefficients are multiplicative rate ratios; under the log link the 2× rescale shifts only the intercept, so the rate ratios are scale-invariant and must not be halved. The correct PWI-vs-AR factor is the unhalved 0.394 (`pscl::zeroinfl` reproduces 0.3941), not 0.197.
- **Errata class:** interpretive. **Severity:** Low. Sign, significance, and the (already-softened) conclusion are unaffected. The body sentence/equation embody the additive treatment-specific-slope reading already retracted by `sec-v1-1-h3b-note`, which does not literally name the 0.197 table cell.
- **Disposition:** **Disclose-only — extend the existing `sec-v1-1-h3b-note`** with one sentence:
  > Relatedly, the exponentiated non-intercept coefficients in @tbl-uce-modsum are scale-invariant rate ratios, so the 2× response rescale cancels for them; the "Adj Coef" halving is meaningful only for the intercept (an expected count). The multiplicative factor relating PWI to the reference AR condition is the exponentiated coefficient itself, 0.394, not the halved 0.197.

#### [DEFERRED] F-009 — Descriptive text misorders the iTCT medians (PAR, not PWI/AR, has the highest)
- **Location:** `_chaps/25-results.qmd:3785` (describing `fig-h3-boxplot`).
- **Issue:** "PWI and AR slightly higher than PAR and MR" — recomputed `median(incr_tct)`: PWI 38.0, PAR 47.5, AR 40.9, MR 16.9. PAR is the maximum; PWI/AR exceed only MR. The parallel UCE-ordering clause in the same sentence is correct.
- **Errata class:** consistency. **Severity:** Low. The iTCT model finds no significant treatment effect, so inference is unaffected.
- **Disposition:** **Defer to a later errata pass / footnote.** Note the correct order PAR (47.5) > AR (40.9) > PWI (38.0) > MR (16.9).

#### [DEFERRED] F-025 — H1c outlier prose claims "a combination of IQR and Z-score" but the code applies IQR only
- **Location:** `_chaps/25-results.qmd:2897`; chunk `h1c-outliers` (`:2877`: `check_outliers(..., method = "iqr", threshold = 1.5)`).
- **Issue:** No Z-score is computed for H1c; the three reported PWI participants (1016, 1017, 1056) reproduce from the IQR fence alone. A literal Z>2.5 test would flag only two of them, so "combination" cannot reproduce the reported three. Z-score is used elsewhere (H2b, the group screen), not here.
- **Errata class:** consistency. **Severity:** Low. The H1c outliers were a robustness check, not removed; no reported n or test result changes.
- **Disposition:** **Defer to a later errata pass / footnote.** Replace with "Tukey's IQR fence (1.5 × IQR)."

#### [DONE] F-016 — Methods refers to "the RQ1 analyses" but research questions are lettered A–E (no numbered RQ1)
- **Location:** `_chaps/24-methods.qmd:329` (tex `:5303`).
- **Issue:** Research questions are enumerated A–E in the Problem Statement; `RQ[0-9]` appears exactly once in the whole corpus, here. The intended referent is the learning-phase (H1) analyses.
- **Errata class:** editorial (orphan label). **Severity:** Low. Meaning recoverable from context.
- **Disposition:** **Fix inline in web build / disclose:** "the RQ1 analyses" → "the learning-phase (H1) analyses."

#### [PENDING] F-020 — Claim that bootstrap resampling "increases the sample size and statistical power" is a methodological misstatement
- **Location:** `_chaps/25-results.qmd:3223` (H2a OEE Analysis).
- **Issue:** Resampling with replacement does not add information, increase effective n, or increase power; the number of resamples affects only Monte-Carlo precision. The sentence sits in the paragraph already addressed by `sec-v1-1-boot-note`, but that note does not cover this overstatement.
- **Errata class:** interpretive. **Severity:** Low. H2a inference rests on Kruskal–Wallis; the bootstrap is a complementary robustness check.
- **Disposition:** **Disclose-only — extend `sec-v1-1-boot-note`:** clarify that resampling improves the precision/characterization of the sampling distribution and CIs but does not increase the effective sample size or statistical power, which are fixed by n and the observed effect.

#### [DONE] F-017 — Double-print "Appendix Appendix F" on the HTML landing page
- **Location:** `index.qmd:5` (rendered `html/index.html:276`, `html/search.json:7`).
- **Issue:** Literal "Appendix " precedes `@sec-v1-1-changelog`, whose auto-text is already "Appendix F — Change Log," yielding the doubled word. HTML-only (callout gated to `when-format="html"`).
- **Errata class:** editorial. **Severity:** Low.
- **Disposition:** **Fix inline in web build:** delete the literal "Appendix " so the source reads "…recorded in @sec-v1-1-changelog."

#### [DONE] F-018 — Double-print "Appendix Appendix F" inside the change-log table
- **Location:** `_apps/39i-v1-1-changelog.qmd:22` (rendered `html/_apps/39i-v1-1-changelog.html:384`, `manuscript/dissertation.tex:13981`).
- **Issue:** Same root cause as F-017; here it appears in both HTML and LaTeX/PDF.
- **Errata class:** editorial. **Severity:** Low.
- **Disposition:** **Fix inline in web build** (same pass as F-017): "direct links to Appendix @sec-v1-1-changelog" → "direct links to @sec-v1-1-changelog." Leave the subsection references (`@sec-v1-1-h3b-note`, `@sec-v1-1-boot-note`) unchanged — they target subsections and render correctly.

#### [DONE] F-026 / F-027 / F-028 / F-029 / F-030 / F-031 / F-032 — Repeated-word, misspelling, and verb-form copy defects (batch)
- **Locations and fixes:**
  - F-026 `_chaps/23-prob_statement.qmd:44` — "the the selection" → "the selection."
  - F-027 `_chaps/22-lit_review.qmd:600` — "the choice to to either" → "the choice to either."
  - F-028 `_chaps/22-lit_review.qmd:600` — "while constructed an 18-step" → "while constructing an 18-step."
  - F-029 `_chaps/22-lit_review.qmd:578/581` — "operator competency is considering" → "is considered."
  - F-030 `_chaps/25-results.qmd:3569/3632/3664` — "Kruskall-Wallis"/"Kurskal-Wallis" → "Kruskal-Wallis" (×3).
  - F-031 `_chaps/25-results.qmd:2897` — "did not impacting" → "did not impact."
  - F-032 `_chaps/25-results.qmd:3146,3569,5038` and `_chaps/26-conclusions.qmd:3` — "with with" / "the the" (×3) → single word.
- **Errata class:** editorial. **Severity:** Low (each). None affects any number, statistic, or claim.
- **Disposition:** **Fix inline in the web build in one batched copy pass, with a single Appendix F roll-up row** (matching the v1.1 P0 precedent that fixed repeated words inline rather than footnoting each). Per-typo footnotes are disproportionate and would clutter the corrected record.
- **Suggested Appendix F roll-up row:** "Results, Conclusions, Problem Statement, and Literature Review prose | residual repeated-word, eponym-spelling, and verb-form typos missed by the v1.1 P0 copy sweep (e.g. 'the the', 'with with', 'to to', 'Kruskall-/Kurskal-Wallis', 'did not impacting', 'while constructed', 'is considering') | corrected inline | editorial cleanup only; no analysis, data, or narrative changed."

#### [DEFERRED] F-034 — Four cited references are skeletal `@article` entries rendering as "(n.d.)"
- **Location:** `references.bib` lines 166, 1117, 2474, 2623 (`army2022ivas`, `etsi2022arf`, `ms2022mrtk`, `opencv2022pnp`); cited at `_chaps/22-lit_review.qmd:366, 460, 707`.
- **Issue:** Title-only entries with no author/year/source render as bare titles plus "(n.d.)." These are load-bearing citations (the $22b IVAS claim, the standards-bodies list, the pose-estimation figure source). Each in-text claim is independently dated in prose.
- **Errata class:** editorial. **Severity:** Low.
- **Disposition:** **Defer to a later errata pass.** Retype as `@online`/`@misc` with organization author, year (each key embeds 2022), URL, and `urldate`. No prose change needed.

#### [DEFERRED] F-035 — Malformed/impossible publication year `{0015/2018-01-17}` in a bib entry
- **Location:** `references.bib:1946` (`konig2018embod`).
- **Issue:** A garbled Zotero-export year (year 15 AD + an ISO date fragment); the true year is 2018 (booktitle/DOI/key confirm). The entry is **uncited** (`grep` finds it nowhere outside `references.bib`), so it never reaches the rendered bibliography.
- **Errata class:** data (source-file only). **Severity:** Low. Not reader-facing.
- **Disposition:** **Disclose-only / source hygiene** — trivial fix to `year = {2018}` on the next clean typesetting pass; not erratum-eligible because nothing renders.

---

## Part 2 — Out-of-scope observations (NOT errata)

These are true but are analysis-choices, recognized statistical-philosophy matters, expected tool behavior, or improvement ideas for the **derived paper / future work**, not defects in the defended record.

- **F-021 — Observed (post-hoc) power presented as independent validation.** At `:1908`, `:3146`, `:3585`, simulated power computed from the study's *own* observed effect size is framed as corroborating reliability. Post-hoc power is a monotone transform of the obtained p-value (Hoenig & Heisey, 2001) and adds no independent support — especially for the non-significant H2b case. The values are computed correctly and the convention is applied consistently; the defender's rejection (analysis-choice, not a computational/factual error) holds. **Future-work fix:** drop or recast the "validates/supports reliability" framing in the derived paper; rely on the design-stage power discussion instead.

- **F-011 — Rank ε²_rank bootstrap CIs pinned at the upper bound 1.0.** H1a [0.4,1.0], H1c [0.32,1.00], H2a [0.08,1.0], H2b [0.07,1.0]. Saturation at 1.0 is the known degeneracy of the percentile bootstrap for a [0,1]-bounded statistic at small n; the values are transcribed faithfully and three of four cases already flag the width verbally. **Future-work idea:** use a bias-corrected/bounded interval method (e.g., BCa or a logit-scale interval) for bounded effect sizes in the derived paper; the point estimates and conclusions are unaffected.

- **F-007 — Across-replication `Sig` rule uses logical OR on proportions.** `Sig = ifelse(mean(CI_Lower>0) | mean(CI_Upper<0), "*", "")` (`:429–431`) would flag significance from ≥1 of five replications rather than a consensus. **Inert** in the defended record because the documented per-replication reseed bug made all five replications bit-identical (`Bias_sd = SE_sd = 0`), so each `mean()` is 0 or 1 and the rule equals the single-replication flag. Subsumed by `sec-v1-1-boot-note`. **Future-work fix:** the corrected bootstrap implementation carried in follow-on work should use a majority/consensus rule.

- **F-006 — Composite reliance "averaging time per reference across all four tasks" implemented as a pooled total/total ratio.** `pwi_time_per_ref_agg = avg_pwi_time/avg_pwi_count = tot_time/tot_count` is a count-weighted (pooled) rate, used consistently everywhere downstream. The large discrepancies versus a "mean of four per-task ratios" arise only under an indefensible zero-fill convention (67% of tasks have zero PWI references). The defender's rejection holds: the pooled rate is a faithful, arguably preferable realization of the prose. **Observation only** — optional one-line clarification ("count-weighted/pooled average") if the author wishes.

- **F-002 — ε²_rank described as "variance in TCT" explained.** Rank epsilon-squared measures variance in the *ranks*, not the original TCT scale. However, "proportion of variance explained" is the standard field gloss (Tomczak & Tomczak 2014; `rstatix`/`effectsize`), applied consistently across H1a–H2b and the SUS analysis, and the numeric value (0.498 ≈ 0.5) is correct. The defender's rejection holds. **Observation only** — the derived paper could insert "in the ranks" for precision.

- **F-012 — Orphaned tracked cache artifacts.** `rdata/h1a.RData` (referenced only under `archive/results-drafts/`) and `rdata/recall.RData` (its `save()`/`load()` commented out at `:2985`/`:3704`; `recall` recomputed live) are tracked but not produced/consumed by any rendered chunk. No output-fidelity risk. **Repo-housekeeping / future-work** item, outside errata scope — optionally untrack on a future cleanup.

---

## Dismissed / considered-and-cleared

The adversarial check rejected these as not real defects; recorded so the author sees what was examined and cleared.

- **F-010 — DHARMa residual diagnostics "run without `set.seed`."** Cleared: `DHARMa::simulateResiduals` self-seeds (`seed=123` default with `on.exit` state restore), so the KS p≈0.03, dispersion p=0.86, and outliers p=0.43 are deterministic and reproduce identically across seeded and unseeded runs. The refit decision is independently carried by the deterministic Shapiro–Wilk test. *(Status: dismissed.)*

- **F-014 — Retention source has 26 records but text says 24 volunteered.** Cleared: the two extra rows (1008, 1010) are pilot participants in the documented, document-wide pilot exclusion (1001–1010). "24" is the correct analysis count and every retention statistic recomputes exactly from it; the v1.1 errata process already verified retention-volunteer accounting and the pilot exclusion. *(Status: dismissed.)*

- **F-024 — "Real-world manufacturing assembly training context" vs a simulated LEGO task / novice convenience sample.** Cleared: an explicitly defended *relative* ecological-validity claim grounded in the authentic Tiger Motors Lean Education Lab and validated instructions, with the convenience-sampling and LEGO-task limitations openly conceded in the Limitations section (`24-methods.qmd:1635, 1641`). Framing/strength rewording is explicitly out of errata scope. *(Status: dismissed.)*

- **F-033 — Leftover TODO "fix double-caption from display_model_parameters."** Cleared: wrapped in a correctly-spelled `::: content-hidden` block (`:2291–2293`); `grep` confirms it renders nowhere. Not a published defect (distinct from the v1.1-corrected *misspelled*-fence leak).

- **F-037 — Hidden authoring note duplicating the Kaplan (2021) summary.** Cleared: inside a correctly-spelled `content-hidden` block (`:739–741`); does not render. The rendered citation at `:725` attributes a genuine Kaplan finding, so the public record is accurate regardless of which facets the visible summary foregrounds.

- **F-036 — Kress (2020) optics monograph cited for a workforce/skilled-labor-shortage claim (`22-lit_review.qmd:450`).** Cleared/unsubstantiated: the book's own abstract frames it around "consumer, enterprise, and defense" displays and "market analyst expectations," so it plausibly carries the enterprise-adoption/workforce framing; the main clause (XR's promise for training) is squarely in scope. Prosecutor was uncertain and recommended drop; defender rejected. A soft citation-rationale judgment, not a verifiable error.

---

## Recommended v1.1.1 action set

The bootstrap per-replication reseed bug (structurally-zero `sd` columns in `tbl-boot-oee`/`tbl-boot-pwi`) is **already handled** via `sec-v1-1-boot-note` + the Results footnote and is not re-litigated here.

**Add to v1.1.1 now — footnote + Appendix F, defended numbers left in place:**
1. **F-003 (mandatory)** — H2b reliance summary wrong magnitudes + inverted direction; flag the parallel Conclusions passages (`26-conclusions.qmd` 34/38/89). This is the one finding that meets the bootstrap-bug bar.
2. **F-004** — OEE PWI–MR 0.307 → 0.614 footnote.
3. **F-019** — Conclusions PAR error-rate contradiction footnote.
4. **F-015** — "controlling for iTCT" → "initial TCT ($TCT_0$)" (inline + Appendix F row).

**Fold inline into the rebuilt web build (no per-item footnotes; one batched Appendix F roll-up row), matching the v1.1 P0 copy/render precedent:**
- F-022 (missing `@` sigil), F-017 + F-018 ("Appendix Appendix F" double-prints), F-016 ("RQ1" orphan label), F-005 (skew word), F-023 (display-name), and the copy cluster F-026–F-032.

**Extend the existing notes (one sentence each), no new structure:**
- F-013 and F-020 → append to `sec-v1-1-h3b-note` and `sec-v1-1-boot-note` respectively.

**Defer to a later errata pass (inert / discarded-branch / non-rendering):**
- F-008 (Poisson BIC, discarded branch), F-009 (iTCT median order), F-025 (IQR-vs-Z-score wording), F-034 (skeletal bib metadata), F-035 (uncited malformed year), F-001 (fixed-vs-random correlation — disclose-only).

**Treat as out-of-scope observations for the derived paper / future work (not errata):**
- F-021, F-011, F-007, F-006, F-002, F-012.

**Ship verdict:** The substantive record is sound — no confirmed finding changes any hypothesis decision, estimate, test, or effect size. Once F-003 (and ideally F-004, F-015, F-019, F-022) are folded in and the batched inline render/copy fixes are applied, **the v1.1.1 release is clear to ship.** F-003 is the single item that should gate the release; everything else is either an inline cleanup that travels with the same build or safely deferrable.

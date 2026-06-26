# v1.1.1 Review — Addendum (Workload/SUS + Abstract)

This addendum folds a focused second pass over the Workload/Usability block (TLX Q1–Q4 and SUS) and the abstract into the main v1.1.1 pre-release review. Adjudication follows the errata-not-revision policy and the rule that a finding is a *confirmed erratum* only where the prosecutor cited concrete evidence and the defender could not defend it; defended records are routed to `disclose_only`/observation. Established facts are honored throughout: PAR was FAST (H1a) and LOW-ERROR (H1c), and Conclusions erratum F-019 already corrects the parallel error of grouping PAR with PWI as high-error.

## Verdict

The Workload/Usability analyses are statistically sound and the abstract's workload claim is correct. A full second-pass recomputation under R 4.4.0 + project renv reproduced every printed number in the TLX/SUS block to displayed precision (TLX composite Task Workload Kruskal–Wallis p = 0.529 → printed 0.53; SUS-learning Kruskal–Wallis p = 0.397 → 0.40 with rank ε² = 0.058 → 0.056; SUS phase-change Wilcoxon p < 0.001, median improvement 31.34, rank-biserial −0.644 [−0.792, −0.424]; TLX Q1 Friedman 122.1, Kendall W = 0.01; Q3 seventeen significant Dunn pairs; Q4 KW p = 0.529; change-by-treatment KW p = 0.479). The abstract's assertion that "no significant differences in perceived workload were found across treatments" is therefore corroborated (TLX Q4 p = 0.53; SUS-learning p = 0.40). No statistical or computational defect exists in this block. The remaining issues are editorial/notation slips plus one interpretive framing concern in the abstract — the dichotomous "augmented … generally led to … slower initial performance" sentence, which mis-sites PAR on the speed axis and is the same misattribution class as confirmed erratum F-019. Because the "generally" hedge gives the abstract sentence a defensible group-level reading, it is routed to disclosure (a footnote parallel to F-019), not a body rewrite.

## Confirmed errata

Ranked by reader-visibility and severity. Suggested corrections are phrased as Appendix-F / v1.1 footnote entries continuing the F-0xx sequence after F-019 (numbers are placeholders).

### [PENDING] 1. Abstract "generally … slower initial performance" mis-sites PAR on the speed axis — disclose_only
- **ids:** G-002, G-003, G-006, G-007 (one finding, four independent confirmations)
- **location:** `_front/12-abstract.qmd` line 7 (Key findings paragraph, para 4)
- **class:** interpretive / consistency · **severity:** low–medium · **disposition:** `disclose_only` (defended record; no body revision)
- **evidence:** Abstract line 7 reads "Augmented technologies generally led to fewer errors but slower initial performance, while traditional methods allowed for faster execution but higher error rates." PAR is listed as an augmented method (`12-abstract.qmd:3`, "Projected AR (PAR)"). Established H1a (`_chaps/25-results.qmd:1874` "'Fast' (PWI, PAR)" / `:1912`; `_chaps/26-conclusions.qmd:19`) places PAR in the FAST group, statistically equivalent to PWI; H1c (`25-results.qmd:2831`; mean UCE 0.76 vs PWI 6.14) places PAR in the LOW-error group. PAR is thus augmented yet fast AND low-error — the favorable exception the speed/accuracy dichotomy erases. This mirrors confirmed Conclusions erratum F-019 (PAR mis-grouped on the error axis) on the speed axis, now in the most-read section.
- **adjudication:** The defender repeatedly and successfully defended the sentence: "generally" is a genuine hedge, 2 of 3 augmented methods (AR, MR — the head-mounted technologies named in the title) were in fact slow, the "fewer errors" half is correct for PAR, the abstract never *names* PAR as slow (unlike the F-019 target text at `26-conclusions.qmd:154`), and the v1.1 changelog explicitly defers "broader rhetorical tightening … beyond the specific corrections documented." Under the adjudication rule this is a defended record → not a text-changing erratum. But given the direct F-019 parallel and the established H1a/H1c facts, transparency warrants a disclosure note rather than silence.
- **suggested correction (Appendix-F style, disclosure only):**
  > **F-020 (Errata — interpretive; disclosure only, abstract text unchanged).** The abstract's "augmented technologies generally led to … slower initial performance" is a hedged group-level generalization. Readers should note that projected AR (PAR), though an augmented method, was among the fast treatments (H1a; statistically equivalent to PWI and faster than AR/MR) while also low-error (H1c; statistically equivalent to AR/MR, mean UCE 0.76). PAR is the fast-and-accurate exception to the speed/accuracy trade-off. This parallels Conclusions erratum F-019, which corrected PAR's mis-grouping on the *error* axis; here the looseness is on the *speed* axis. Per errata-not-revision, the abstract body is not rewritten.

### [DONE] 2. SUS phase-change effect size printed as a squared quantity but negative — fold_v111
- **ids:** G-001, G-012 (duplicate confirmations of one defect)
- **location:** `_chaps/25-results.qmd` line 4787 (`fig-sus-change` prose)
- **class:** editorial / statistical notation · **severity:** low · **disposition:** `fold_v111`
- **evidence:** Prints "The large negative effect size ($\hat{r}^{2}_{biserial}$ = -0.644) … 95% confidence interval [-0.792, -0.424]." A squared correlation is non-negative by definition, so a *squared* effect of −0.644 is mathematically impossible and internally self-contradictory ("squared" and "negative" at once). The value is the signed matched-pairs rank-biserial correlation r that `statsExpressions::two_sample_test(paired=TRUE, type='nonparametric')` (via `ggwithinstats`, set.seed(42)) labels "r (rank biserial)": estimate −0.6439216, CI [−0.7921607, −0.4239378]. The adjacent line 4785 correctly uses a genuinely squared measure, $\hat{\varepsilon}^{2}_{rank}$ = 0.056, and line 4888 correctly writes the same effect-size family as "$r$ > 0.50," confirming the superscript was carried over in error.
- **suggested correction:**
  > **F-021 (Errata — editorial).** `25-results.qmd:4787`: change "$\hat{r}^{2}_{biserial}$ = -0.644" to "$\hat{r}_{biserial}$ = -0.644" (matched-pairs rank-biserial correlation). The value −0.644, CI [−0.792, −0.424], and the "large negative effect" interpretation are correct and unchanged.

### [DONE] 3. Broken cross-reference — literal "fig-tlx-q2-heat" prints instead of a figure number — fold_v111
- **id:** G-008
- **location:** `_chaps/25-results.qmd` line 4526 (renders `html/_chaps/25-results.html:5086`)
- **class:** editorial · **severity:** low–medium · **disposition:** `fold_v111`
- **evidence:** Source reads "…explored changes across the treatment axis of fig-tlx-q2-heat for unweighted source ratings…" with the cross-reference missing its leading `@`, so Quarto does not resolve it; the rendered HTML prints the raw label "fig-tlx-q2-heat" mid-sentence, immediately beside a working `@fig-tlx-q3-bar` → "Figure 5.37". The label is valid (chunk defined `25-results.qmd:4464`; correctly referenced `@fig-tlx-q2-heat` at `25-results.qmd:4427` → Figure 5.36).
- **suggested correction:**
  > **F-022 (Errata — editorial).** `25-results.qmd:4526`: insert the missing `@` so "fig-tlx-q2-heat" reads "@fig-tlx-q2-heat", resolving to Figure 5.36 (the heatmap). One-character fix; no statistic affected.

### [DONE] 4. Misspelled NASA-TLX citation "Heart 2006" (should be "Hart") — fold_v111
- **id:** G-011
- **location:** `_chaps/25-results.qmd` line 4423 (renders `html/_chaps/25-results.html:5066`)
- **class:** editorial · **severity:** low · **disposition:** `fold_v111`
- **evidence:** "…it remains the officially recommended methodology *(Heart 2006)*." The NASA-TLX author is Sandra G. Hart; `references.bib:1400` defines `hart2006tlx` with `author = {Hart, Sandra G.}`, and `_chaps/22-lit_review.qmd:799` cites the same work correctly as `@hart2006tlx`. The reference is also typeset as italic inline text rather than a Quarto citation, unlike the rest of the document, but the surname is the load-bearing error.
- **suggested correction:**
  > **F-023 (Errata — editorial).** `25-results.qmd:4423`: change "(Heart 2006)" to "(Hart 2006)"; ideally convert the two italic pseudo-citations in the sentence to proper Quarto keys (`@hart2006tlx`) to match the rest of the document.
- **resolution (v1.1.1):** Fixed Heart → Hart and converted that pseudo-citation to `[@hart2006tlx]` (now renders "(Hart, 2006)"). The companion pseudo-citation in the same sentence, *(Bustamante and Spain 2008, Byers et al 1989)*, is **not** in `references.bib` (grep confirms), so it cannot be converted without adding two new bibliography entries. It is left as italic text and deferred to a future bibliography/Zotero pass, after which it can become a proper citation as well.

### [DEFERRED] 5. Figure 5.41 caption is a copy of Figure 5.40's and does not describe its content — defer
- **id:** G-009
- **location:** `_chaps/25-results.qmd` fig-cap line 4891 (`fig-sus-within-trt`, Figure 5.41); duplicate of line 4790 (`fig-sus-change`, Figure 5.40)
- **class:** consistency / editorial · **severity:** low · **disposition:** `defer_errata`
- **evidence:** Both figures carry the identical caption "System Usability Score for Learning and Recall Phases" (`html/_chaps/25-results.html:5254` and `:5284`). That caption fits Figure 5.40 (within-subject paired phase change, `ggwithinstats`) but not Figure 5.41, which plots the between-treatment comparison of the SUS change (`ggbetweenstats` on `diff ~ treatment`, in-plot title "Is there a Treatment Effect on the Change in SUS between Phases?", subtitle p = 0.479). The figure remains correctly interpretable from its own title, subtitle, and the introducing sentence at line 4888, so no reader is misled — hence defer rather than fold.
- **suggested correction:**
  > **F-024 (Errata — editorial).** `25-results.qmd:4891`: replace the `fig-cap` for `fig-sus-within-trt` with one describing its content, e.g. "Between-Treatment Comparison of the Change in SUS from Learning to Recall." Caption-only; no code, data, or statistic affected. Figure 5.40's caption is unchanged.

### [DEFERRED] 6. TLX Q2 boundary statements marginally false at the extreme treatment — defer
- **id:** G-004
- **location:** `_chaps/25-results.qmd` line 4427 (TLX Q2 narrative)
- **class:** editorial · **severity:** low · **disposition:** `defer_errata`
- **evidence:** The text says Temporal Demand means are "all above 66.1" and Physical Demand means "all below 25.8." Recomputed per-treatment means (the `fig-tlx-q2-heat` quantities, R 4.4.0/renv, `combined_results.xlsx`, phase 1): TD AR 80.36, PAR 71.25, MR 68.57, PWI 66.07 → min 66.07 < 66.1; PD PAR 25.83, PWI 23.93, MR 22.07, AR 16.79 → max 25.83 > 25.8. Both extreme cells cross the cited thresholds in the wrong direction, and the heatmap's own 1-decimal labels show PWI TD = 66.1 and PAR PD = 25.8 (equal, not exceeding). The qualitative point (TD highest, PD lowest in every group) is unaffected.
- **suggested correction:**
  > **F-025 (Errata — editorial).** `25-results.qmd:4427`: change "all above 66.1" to "all above 66" (min 66.07) and "all below 25.8" to "all below 26" (max 25.83), or use non-strict inequalities ("at or above 66.1" / "at or below 25.8"). No figure value or conclusion changes.

### [DONE] 7. SUS acronym expanded as "Score" (should be "Scale") — defer
- **id:** G-010
- **location:** `_chaps/25-results.qmd` line 4717
- **class:** consistency / editorial · **severity:** low · **disposition:** `defer_errata`
- **evidence:** "The System Usability Score (SUS) provides a complementary view…" expands the acronym as "Score." SUS = System Usability *Scale* (Brooke, 1996); the score is its numeric output. This contradicts the section header "### System Usability Scale Analysis" (`25-results.qmd:4647`) and the abstract (`12-abstract.qmd:5`), both of which use "Scale." Localized first-use slip; zero analytical consequence.
- **suggested correction:**
  > **F-026 (Errata — editorial).** `25-results.qmd:4717`: change "The System Usability Score (SUS)" to "The System Usability Scale (SUS)".

### [DONE] 8. Repeated/extra article: "from the those observed" — fold_v111
- **id:** G-013
- **location:** `_chaps/25-results.qmd` line 4267
- **class:** editorial · **severity:** low · **disposition:** `fold_v111`
- **evidence:** "…and how those measures differ from the those observed during recall." The stray "the" before "those" is ungrammatical and appears verbatim in `search.json` / rendered output. No defensible reading.
- **suggested correction:**
  > **F-027 (Errata — editorial).** `25-results.qmd:4267`: delete the stray "the" — "…differ from those observed during recall."

### [DONE] 9. Three minor grammar/spelling errors in the workload/usability prose — defer
- **id:** G-015
- **location:** `_chaps/25-results.qmd` lines 4423, 4427, 4741
- **class:** editorial · **severity:** low · **disposition:** `defer_errata`
- **evidence:** (a) `4423` "has lead other researchers" → "has led"; (b) `4427` "Temporal Demand consistently rate as the most important workload source" → "rates" (subject–verb agreement; contrast the parallel correct "Physical Demand is consistently rated" in the same paragraph); (c) `4741` "will have no affect on the statistical conclusions" → "effect" (affect/effect). All three reproduce in rendered HTML; none touches a number or claim.
- **suggested correction:**
  > **F-028 (Errata — editorial).** `25-results.qmd`: line 4423 "has lead" → "has led"; line 4427 "consistently rate" → "consistently rates"; line 4741 "no affect" → "no effect."

## Observations / dismissed

- **G-005 — verification, no defect (supports the verdict).** Second-pass recomputation reproduced every printed TLX/SUS value to displayed precision, and the abstract's "no significant differences in perceived workload" claim is directly supported (TLX Q4 KW p = 0.53; SUS-learning KW p = 0.40). No statistical defect in the block. This is corroboration, not an errata candidate.
- **G-014 — malformed lead-in "aspects of that influence workload during learning" (`25-results.qmd:4324`) — DEFENDED → no errata.** The prosecutor read it as missing words; the defender supplied a valid parse ("aspects of that [matter], which influence workload") given the preceding sentence and the Q1–Q4 list that follows. Defended record; meaning is unambiguous. At most a `disclose_only` smoothing if an editorial pass is already open ("…aspects of that influence on workload during learning:"); not worth altering the defended record on its own.
- **Abstract PAR framing — defense acknowledged.** The defender's "generally"-hedge reading (item 1 above) was accepted as legitimate, which is precisely why item 1 is routed to `disclose_only` (footnote parallel to F-019) rather than a body rewrite. Recorded here so the disposition is transparent: it is a disclosed interpretive note, not a confirmed text-changing erratum.

## Updated ship guidance

This addendum does not change the main report's recommendation: the Workload/Usability block is statistically sound and contains no computational, data, or inferential defect, and the abstract's workload claim is correct. All confirmed items are editorial/notation or interpretive-disclosure — none is a ship blocker. Recommendation: **SHIP v1.1.1 with errata.** Concretely:

1. **Fold into the v1.1.1 build (trivial, zero-substance fixes):** the spurious `r²` superscript (F-021), the missing `@` cross-reference (F-022), Heart → Hart (F-023), and the "from the those" stray article (F-027).
2. **Document as Appendix-F errata entries (correct without substantive change):** Figure 5.41 caption (F-024), TLX Q2 boundary wording (F-025), SUS Score → Scale (F-026), and the grammar trio (F-028).
3. **Add one disclosure footnote, no body rewrite (errata-not-revision):** the abstract's "generally … slower" speed-axis framing (F-020), explicitly tied to F-019, surfacing PAR as the fast-and-low-error exception. This is the single item warranting "special attention" because it sits in the most-read section and recapitulates the F-019 misattribution class; the "generally" hedge keeps it out of mandatory-correction territory but transparency favors disclosing it.

No item delays release. The block's substance — including the headline SUS phase-change improvement and the null workload result behind the abstract claim — stands as published.

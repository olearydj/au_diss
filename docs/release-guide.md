# Dissertation Release Guide

## Purpose

Step-by-step procedure for cutting a corrected release of the dissertation: source on a tag in `olearydj/au_diss`, the rebuilt PDF as a GitHub Release asset, and the rebuilt HTML published to `olearydj/blog`. This records the proven `v1.1.1` process and the non-obvious pitfalls hit along the way. For the build path and bibliography provenance see `docs/build.md`; for the errata-versus-revision policy see `docs/v1-1-errata-checklist.md`.

## Governing principle

Post-`v1.1` corrections are errata, not revisions. Never change an analytic decision to improve a result; disclose it (a footnote plus an Appendix F change-log entry, defended numbers preserved) and, where useful, add a sensitivity check. Any correction that alters a rendered value should be produced by inline R, not hand-typed, the surviving errors in `v1.1.1` were all in transcribed prose, never in the computed pipeline.

## Publishing model

- `au_diss` ships source only on the tag. `html/` and `manuscript/` are gitignored and generated on demand.
- The rebuilt PDF is the single asset on a GitHub Release: asset filename `dissertation.pdf`, display label `oleary-dissertation-vX.Y.Z.pdf`.
- The rebuilt HTML is published in the separate `olearydj/blog` repo under `dissertation/` (tracked via a `.gitignore` exception); pushing `main` deploys the site.
- The as-defended PDF stays at its own Release (`baseline/dissertation-defended-2024-08-02`); each errata release links back to it.

## Prerequisites

- R 4.4.0 via `rig`. The render is pinned to 4.4.0 by the `_environment` file (`QUARTO_R=/Library/Frameworks/R.framework/Versions/4.4-arm64/Resources/bin/Rscript`). rig's default is R 4.5.3; do not render under it, the `renv` library is built for 4.4.0 and mismatches under 4.5.x. If you render outside the project's env loading, prepend the 4.4 bin to `PATH` as a belt-and-suspenders.
- Quarto (1.9.x) and MacTeX / LuaLaTeX (TeX Live).
- `gh` authenticated as `olearydj`.
- `references.bib` is generated from the Zotero collection "dissertation" (collection id 26, including its subcollections, 292 entries as of `v1.1.1`) via Better BibTeX. Its auto-export was disabled as of `v1.1.1`; regenerate manually when citations change. See `docs/build.md` (Bibliography Source). Do not hand-edit `references.bib`.

## Procedure

The commands below cut `vX.Y.Z`; the `v1.1.1` run is the reference. Run renders in a shell with the project environment loaded (so `_environment` sets `QUARTO_R`); if a sandbox is in play, disable it, a sandboxed R run produced a spurious segfault.

### 1. Land source edits on an errata branch

Work on `vX.Y.Z-errata`. Update the two release-identity spots:

- `index.qmd` landing callout (`.callout-note`): describe the actual scope of the release. Do not understate it, `v1.1.1`'s callout originally said "one further correction" when the release corrected the recall reliance direction, the OEE misprint, the H3b rescaling, and more.
- `tex/titlepage.tex` release line: set the date to the actual release date.

### 2. Render HTML then PDF

```bash
quarto render --to html --profile html
quarto render --to pdf --profile pdf
```

Both exit 0. Confirm the R version in the log reads 4.4.0. Outputs: `html/index.html` and `manuscript/dissertation.pdf` (~100 MB).

### 3. Restore the render side-effect

```bash
git checkout -- rdata/shared.RData
```

Every render re-saves this tracked file; always restore it before committing.

### 4. Verification gates

Cross-reference double-print gate, over the whole HTML tree (the book nests chapters under `html/_chaps/` and `html/_apps/`, so `html/*.html` alone only scans the landing page):

```bash
find html -name '*.html' | while read f; do sed 's/<[^>]*>//g' "$f"; done \
  | grep -nE "Appendix Appendix|Appendix Section|Section Section"
pdftotext manuscript/dissertation.pdf - | grep -nE "Appendix Appendix|Appendix Section|Section Section"
```

The only acceptable hit is the Appendix F change-log row that quotes the fixed `"Appendix Appendix F"` defect as a description. Strip tags first; a raw-HTML grep misses these because an `<a>` tag sits between the two words.

No leaked internal source filenames in reader-facing text:

```bash
pdftotext manuscript/dissertation.pdf - | grep -c '\.qmd'        # want 0
```

Appendix F change-register tables, inspect for column overflow (a space-less monospace token can overrun its column). Render the pages to images and look:

```bash
pg=$(pdftotext manuscript/dissertation.pdf - | awk -v RS=$'\f' '/Issue in defended/{print NR; exit}')
pdftoppm -png -r 120 -f "$pg" -l $((pg+3)) manuscript/dissertation.pdf /tmp/cr
```

PDF title-page date baked correctly:

```bash
pdftotext -f 1 -l 1 manuscript/dissertation.pdf - | grep "corrected release"
```

### 5. Commit on the errata branch

Commit the source edits (e.g., the callout and title-page date) on `vX.Y.Z-errata`.

### 6. Fast-forward master and tag

```bash
git checkout master
git merge --ff-only vX.Y.Z-errata
git tag -a vX.Y.Z -m "Dissertation vX.Y.Z - errata point release

<one-paragraph scope summary>. No new data or analyses; no hypothesis
determination changes. Full change log in Appendix F."
```

### 7. Push source and tag

```bash
git push origin master
git push origin vX.Y.Z
```

### 8. GitHub Release

Match the asset convention exactly: filename `dissertation.pdf`, label `oleary-dissertation-vX.Y.Z.pdf`. Mark it Latest (demotes the prior release). The PDF is large, so the upload takes a moment.

```bash
gh release create vX.Y.Z \
  --repo olearydj/au_diss \
  --title "Dissertation vX.Y.Z" \
  --notes-file <notes.md> \
  --latest \
  "manuscript/dissertation.pdf#oleary-dissertation-vX.Y.Z.pdf"

gh api repos/olearydj/au_diss/releases/latest --jq .tag_name   # confirm vX.Y.Z
```

Release notes should state the scope, link the `vA.B.C...vX.Y.Z` compare view, and link the as-defended baseline release.

### 9. Publish HTML to the blog

```bash
rsync -a --delete html/ /casa/pub/blog/dissertation/
cd /casa/pub/blog
git add -A dissertation
git diff --cached --name-status dissertation | awk '{print $1}' | sort | uniq -c   # preview
```

Sanity-check the staged diff before committing: expect modified content pages plus the occasional Quarto asset-hash bump (and a rename if a chapter/appendix file was renamed). A mass deletion means `html/` was empty or wrong, abort. Then:

```bash
git commit -m "Publish dissertation vX.Y.Z"
git push origin main
```

## Pitfalls (learned in v1.1.1)

- rig's default R is 4.5.3; renders must use 4.4.0. The `_environment` file pins it via `QUARTO_R`; trust that over the shell default.
- The cross-reference gate must scan `html/_chaps` and `html/_apps`, not just `html/*.html` (which is only the landing page).
- A div with a CSS `style="font-size: ..."` only shrinks the HTML table; the PDF (LaTeX longtable) ignores it. For the PDF, wrap the table in raw LaTeX `\begingroup\footnotesize ... \endgroup`, and reallocate column widths through the relative dash counts in the markdown separator row (Pandoc maps them to longtable column widths). A space-less monospace token such as `compare_performance()` will not break and overflows a too-narrow column.
- Cross-reference tokens auto-render their label: `@sec-v1-1-changelog` renders "Appendix F" and `@sec-v1-1-*-note` render "Section F.2.x". Never put a literal "Appendix" or "Section" before them, or you get "Appendix Appendix F". Verify with the tag-stripped grep above.
- Keep internal source filenames (for example `25-results.qmd`) out of reader-facing prose; refer to section names instead.
- Each render re-saves `rdata/shared.RData`; restore it before committing.
- Release asset: GitHub uses the file basename (`dissertation.pdf`) as the asset name and the `#label` as the display alias.

## Related docs

- `docs/build.md` - canonical build path, environment capture, and `references.bib` provenance.
- `docs/v1-1-errata-checklist.md` - the errata-versus-revision policy and the v1.1 precedent.
- `docs/dissertation-v111-review.md` and its addendum - the v1.1.1 finding register with per-item status.
- `_apps/39i-changelog.qmd` - Appendix F (Change Log); the reader-facing record of every correction.

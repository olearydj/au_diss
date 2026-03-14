# TeX And PDF Build Dependencies

This document tracks non-R dependencies discovered while rebuilding the dissertation PDF on the current machine.

## Current TeX Context

- TeX distribution: BasicTeX / TeX Live 2026
- `tlmgr` installation root: `/usr/local/texlive/2026basic`
- TeX setup notes for this machine:
  [/Volumes/Casa/pub/blog/posts/2025-10-26-tex-setup/index.qmd](/Volumes/Casa/pub/blog/posts/2025-10-26-tex-setup/index.qmd)

The guiding rule for this machine is to keep TeX management consistent with that setup:

- prefer system-level `sudo tlmgr install <package>`
- avoid introducing a parallel `tlmgr --usermode` tree unless there is a clear reason

The most useful machine-level evidence for the package-recovery sequence is:

- `/usr/local/texlive/2026basic/texmf-var/web2c/tlmgr.log`

That log records the actual install order from the rebuild session and is more authoritative than memory for the whack-a-mole phase.

## Non-R Build Dependencies Found So Far

### System Tools

| Dependency | Status | Notes |
| --- | --- | --- |
| `rsvg-convert` | installed | Required by Quarto to convert SVG figures to PDF for LaTeX output |
| `Source Code Pro` | missing, then required | Required as the configured PDF `monofont` in [_quarto.yml](/Volumes/Casa/pub/dissertation/_quarto.yml#L108); Quarto's fallback package search was misleading because this is a system font, not a TeX package |

Verification:

```sh
which rsvg-convert
rsvg-convert --version
```

For the font requirement:

```sh
brew install --cask font-source-code-pro
```

If LuaLaTeX still cannot find the font after installation, rebuild the Lua font database and rerun the render:

```sh
luaotfload-tool --update --force
```

### TeX Packages Added

| Package | Installed via | Why it was needed |
| --- | --- | --- |
| `scrhack` | `sudo tlmgr install scrhack` | Missing during LaTeX render; Quarto attempted auto-install and failed because the TeX installation was not writable without admin rights |
| `setspaceenhanced` | `sudo tlmgr install setspaceenhanced` | Missing during a later PDF render pass |
| `lualatex-math` | `sudo tlmgr install lualatex-math` | Missing during a later LuaLaTeX render pass |
| `framed` | `sudo tlmgr install framed` | Missing during a later PDF render pass |
| `biblatex` | `sudo tlmgr install biblatex` | Missing during a later PDF render pass |
| `biblatex-apa` | `sudo tlmgr install biblatex-apa` | Missing during bibliography/style resolution for APA output |
| `multirow` | `sudo tlmgr install multirow` | Missing during a later table-rendering pass |
| `floatbytocbasic` | installed during whack-a-mole loop | Confirmed by `tlmgr.log`; needed by the current table/float stack |
| `lscapeenhanced` | installed during whack-a-mole loop | Confirmed by `tlmgr.log`; used by `pdflscape` during the successful build |
| `tabu` | installed during whack-a-mole loop | Confirmed by `tlmgr.log`; used by the successful table stack |
| `varwidth` | installed during whack-a-mole loop | Confirmed by `tlmgr.log`; used with `tabu`/table rendering |
| `threeparttable` | `sudo tlmgr install threeparttable` | Missing during a later table-rendering pass |
| `threeparttablex` | installed during whack-a-mole loop | Confirmed by `tlmgr.log`; used by the successful table stack |
| `wrapfig` | `sudo tlmgr install wrapfig` | Missing during a later layout/render pass |
| `selnolig` | `sudo tlmgr install selnolig` | Missing during a later LuaLaTeX render pass |
| `biber` | installed during collection-based recovery | Confirmed by `tlmgr.log`; required for bibliography generation on this machine |

`tlmgr.log` also confirms that `logreq` was installed automatically alongside `biblatex`.

## Broader Collection Installs

After the one-at-a-time package loop became too slow, larger TeX collections were installed pragmatically to finish the build:

- `collection-latexextra`
- `collection-bibtexextra`

The `tlmgr.log` record also shows:

- `collection-pictures` was pulled in alongside `collection-latexextra`
- the bibliography-collection pass installed `biber` / `biber.universal-darwin` and a large number of bibliography-related packages, many of which are not actually used by this dissertation

These collection installs helped complete the render, but they are not a good proxy for the actual package footprint of the dissertation. The actual used-package set should be extracted from the successful build artifacts and documented separately.

That actual successful-build footprint is now documented in:
[tex-package-footprint-2026-03-12.md](/Volumes/Casa/pub/dissertation/docs/tex-package-footprint-2026-03-12.md)

## TeX Maintenance Notes

Before installing missing packages with `sudo tlmgr install ...`, the TeX Live manager itself had to be updated:

```sh
sudo tlmgr update --self
```

That was required because `tlmgr` refused package installation until `texlive.infra` was updated.

`tlmgr.log` confirms that this happened first:

- `update: texlive.infra (78218 -> 78313)` on `2026-03-11 19:17:16`

## Current Practice During Rebuild

When the PDF build fails on a missing `.sty` file or missing TeX package:

1. identify the package name from the error
2. install it with `sudo tlmgr install <package>`
3. rerun the Quarto render
4. append the package here

This keeps the dissertation source unchanged while documenting exactly what the current machine needed in order to rebuild the defended manuscript.

# TeX Package Footprint (2026-03-12)

## Purpose

This note records the **actual TeX inputs loaded by a successful dissertation build**, as opposed to the much larger set of packages installed on the machine after `collection-latexextra` and `collection-bibtexextra` were added.

The goal is to preserve the real document footprint before later cleanup decisions.

## Source Artifacts

The footprint below was derived from:

- generated TeX source kept by Quarto:
  `Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.tex`
- a direct recorder pass on that TeX source:
  `Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.fls`
- supporting compile log:
  `Augmented-vs.-Traditional-Instruction-in-Manufacturing-Assembly.log`
- supporting TeX Live install history:
  `/usr/local/texlive/2026basic/texmf-var/web2c/tlmgr.log`

The direct recorder pass used `lualatex -recorder` with writable cache paths under `/tmp` so the file list would be preserved.

The `tlmgr.log` file is not part of the document footprint itself, but it is useful corroborating evidence for which packages were surfaced manually during the recovery process versus pulled in later by collection installs.

## High-Level Result

The successful build loaded `120` unique TeX inputs with extensions in:

- `.cls`
- `.sty`
- `.cfg`
- `.bbx`
- `.cbx`
- `.dbx`
- `.lbx`

## Configured System Fonts Confirmed In The Build

The PDF config in [_quarto.yml](/Volumes/Casa/dev/dissertation/_quarto.yml) specifies:

- `mainfont: Georgia`
- `sansfont: Verdana`
- `monofont: Source Code Pro`

Those fonts were confirmed in the `.fls` file as:

- `/System/Library/Fonts/Supplemental/Georgia.ttf`
- `/System/Library/Fonts/Supplemental/Georgia Bold.ttf`
- `/System/Library/Fonts/Supplemental/Georgia Italic.ttf`
- `/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf`
- `/System/Library/Fonts/Supplemental/Verdana.ttf`
- `/System/Library/Fonts/Supplemental/Verdana Bold.ttf`
- `/System/Library/Fonts/Supplemental/Verdana Italic.ttf`
- `/System/Library/Fonts/Supplemental/Verdana Bold Italic.ttf`
- `/Users/djo/Library/Fonts/SourceCodePro[wght].ttf`
- `/Users/djo/Library/Fonts/SourceCodePro-Italic[wght].ttf`

## Actual Loaded TeX Package Families

The document loaded inputs from these package/group paths during a successful build:

```text
generic/bigintcalc
generic/bitset
generic/gettitlestring
generic/iftex
generic/infwarerr
generic/intcalc
generic/kvdefinekeys
generic/ltxcmds
generic/pdfescape
generic/pdftexcmds
generic/stringenc
generic/ulem
generic/uniquecounter
latex/amsfonts
latex/amsmath
latex/base
latex/biblatex
latex/biblatex-apa
latex/bookmark
latex/booktabs
latex/caption
latex/colortbl
latex/environ
latex/epstopdf-pkg
latex/etoolbox
latex/fancyvrb
latex/float
latex/floatbytocbasic
latex/fontspec
latex/footnotehyper
latex/framed
latex/geometry
latex/graphics
latex/graphics-cfg
latex/hycolor
latex/hyperref
latex/koma-script
latex/kvoptions
latex/kvsetkeys
latex/l3kernel
latex/l3packages/l3keys2e
latex/l3packages/xparse
latex/latexconfig
latex/lm
latex/logreq
latex/lscapeenhanced
latex/makecell
latex/microtype
latex/multirow
latex/ninecolors
latex/pdflscape
latex/refcount
latex/rerunfilecheck
latex/scrhack
latex/setspace
latex/setspaceenhanced
latex/siunitx
latex/tabu
latex/tabularray
latex/threeparttable
latex/threeparttablex
latex/tools
latex/translations
latex/trimspaces
latex/unicode-math
latex/upquote
latex/url
latex/varwidth
latex/wrapfig
latex/xcolor
latex/xpatch
latex/xurl
lualatex/lualatex-math
lualatex/selnolig
luatex/ctablestack
luatex/luatexbase
```

## Practical Interpretation

This footprint confirms that the dissertation build actually depends on:

- the KOMA-Script book/class stack
- LuaLaTeX font handling (`fontspec`, `unicode-math`, `lualatex-math`)
- the bibliography stack (`biblatex`, `biblatex-apa`)
- the longtable/caption/table stack used heavily by the Results chapter
- hyperlink/bookmark infrastructure
- the configured system fonts above

It also confirms that the document uses packages that were discovered manually during rebuild, including:

- `scrhack`
- `setspaceenhanced`
- `lualatex-math`
- `framed`
- `biblatex`
- `biblatex-apa`
- `multirow`
- `threeparttable`
- `wrapfig`
- `selnolig`

## Relation To Broader TeX Installs

Later in the rebuild process, these broader TeX collections were installed pragmatically:

- `collection-latexextra`
- `collection-bibtexextra`

Those collection installs were useful for finishing the build, but they are broader than the actual dissertation footprint. The file families listed above are the better record of what this document actually loaded in a successful compile.

## Baseline Implication

For baselining purposes:

- treat this note as the actual LaTeX package-footprint record for the successful 2026-03-12 rebuild
- treat [tex-dependencies.md](/Volumes/Casa/dev/dissertation/docs/tex-dependencies.md) as the record of packages and tools that had to be surfaced during recovery on this machine
- do not infer that every package in `collection-latexextra` or `collection-bibtexextra` is required by this dissertation

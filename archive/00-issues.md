# Issues List

## New Stuff

- Change Appendix titles to be of the form "Appendix A - IRB"
- review all acronyms; add list?
- move weblinks to a consolidated list in appendices?
- define and standardize use of Principle Investigator / PI
- eliminate references to positioning of images, e.g. the image below
- center figure captions?
- standard method for stating image source - inline, or second line of caption? add linebreak in figure caption (PDF)?
- check for consistent useage of XR and AR/MR
- use cool ✓

## Writing Notes

- add paper about updated M&K's Virtuality Continuum? @skarbez2021revis
- hands-free operation is a requirement not affordance
- goal of training = certified operator
  - what makes them certified? complete task correctly in takt time
  - did they learn it? → learning curve
  - can they apply it? → recall errors and times
  - did it stick? → retention
  - what role does proficiency play in this?

## Template Issues

- Fix table of contents
  - Entries are generally double-spaced
  - titles and headings of >1 line are indented at the second line & single-spaced
- List of Abbreviations / Symbols (aka "Nomenclature")
- Font options
- Make title page dynamic (variables)
- Convert vspace amounts to use line heights? use `ex` or other proportional unit
- Change heading style for main chapters
- Indent first line of Abstract and Acknowledgements?

## Quarto / RStudio Issues and Requests

-   Q: Why is index.qmd required for book?
-   Q: How do I turn off ligatures in R Studio?
-   FR: allow project `execute-dir` option to specify a path like `output-dir`
    -   When using the PDF option `pdf-engine-opt: -output-directory=work` for the `xelatex` renderer, the build fails during "updating existing packages" with the error `compilation failed- missing packages (automatic installation failed)`. The files appear to be correctly written to my work directory, but it doesn't know to find them there.
-   When editing a list in a markdown file (either `.md` or `.qmd`), if I switch from source to visual mode and back, all indents become 4 spaces and all text is separated from the hyphens by 3 spaces.
    -   This switch also blew away a markdown formatted link.


how to accelerate PDF render - caching?

**Before:**

``` markdown
- Fix headers and footers
- Change fonts:
  - body
  - headers
```

**After:**

``` markdown
-   Fix headers and footers
-   Change fonts:
    -   body
    -   headers
```

## Archive

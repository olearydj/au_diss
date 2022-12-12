# Issues List

## Template Issues

-   Fix headers and footers
-   Change fonts:
    -   body
    -   headers
-   Missing characters in equations on page 4, section 2.1
    -   ellipsis ($\ldots$), mu ($\mu$), sigma ($\sigma$), infinity ($\infty$), summation ($\Sigma$), square root ($\sqrt{}$), minus ($-$), and script N ($\mathcal{N}$)
-   Can't figure out how to include an abstract

## Quarto / RStudio Issues

-   When editing a list in a plain markdown file (`.md`), if I switch from source to visual mode and back, all indents become 4 spaces and all text is separated from the hyphens by 3 spaces.

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

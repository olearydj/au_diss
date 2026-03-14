# Quarto Config Variants

This folder preserves inactive Quarto project config variants from the
dissertation drafting period.

These files are not part of the active build path. The active manuscript build
uses only the root [`_quarto.yml`](/Volumes/Casa/dev/dissertation/_quarto.yml).

## Why These Exist

While the dissertation was being written, full Quarto renders were slow enough
that the project was sometimes split into smaller manual build targets.

The archived configs document that workflow:

- [`_quarto-full.yml`](/Volumes/Casa/dev/dissertation/archive/quarto-config-variants/_quarto-full.yml) preserves the full-book config variant used for complete PDF builds.
- [`_quarto-part.yml`](/Volumes/Casa/dev/dissertation/archive/quarto-config-variants/_quarto-part.yml) preserves the partial-build base config used with smaller chapter subsets.
- [`_quarto-book.yml`](/Volumes/Casa/dev/dissertation/archive/quarto-config-variants/_quarto-book.yml) preserves one manual chapter-list variant for limited builds.
- [`_quarto-chap.yml`](/Volumes/Casa/dev/dissertation/archive/quarto-config-variants/_quarto-chap.yml) preserves another manual chapter-list variant for limited builds.
- [`_quarto-orig.yml`](/Volumes/Casa/dev/dissertation/archive/quarto-config-variants/_quarto-orig.yml) preserves an older/original project config snapshot.

## Relationship To The Current Repo

- these files are historical workflow support material, not active project infrastructure
- they should not be edited as part of normal dissertation maintenance
- if they are ever useful again, it should be for historical reference only, not as the default build mechanism

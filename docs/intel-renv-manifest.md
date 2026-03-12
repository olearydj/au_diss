# Intel `renv` Manifest

This document records what can still be recovered from the preserved Intel project library at [`renv/library/macos/R-4.4/x86_64-apple-darwin20`](/Volumes/Casa/dev/dissertation/renv/library/macos/R-4.4/x86_64-apple-darwin20).

## Purpose

The checked-in [`renv.lock`](/Volumes/Casa/dev/dissertation/renv.lock) is not a complete record of the package set used to build the dissertation. The strongest local evidence for the old working package set is now:

1. the preserved Intel `renv` library
2. the versions recorded in `renv.lock`
3. git history around the May-August 2024 build window

This manifest is a forensic aid for baseline reconstruction. It is not proof of a byte-identical build environment.

## Why The Lockfile Is Incomplete

The repo previously contained a `clean_packages.R` utility that used `renv::dependencies()` to identify packages and then removed anything not detected. That approach misses packages referenced indirectly, namespaced inside code chunks, or otherwise not discovered cleanly. As a result, important packages used by the authoritative results chapter were installed in the old environment but never reliably captured in `renv.lock`.

## Summary

- Intel library root examined: [`renv/library/macos/R-4.4/x86_64-apple-darwin20`](/Volumes/Casa/dev/dissertation/renv/library/macos/R-4.4/x86_64-apple-darwin20)
- Entries present in that library root: `411`
- Package-like entries excluding `.renv`: `410`
- Entries still locally readable as full package directories: `40`
- Entries preserved only as broken symlinks into the old renv cache: `371`

The broken symlinks are still useful because the target path encodes package name and version, for example:

```text
.../renv/cache/v5/macos/R-4.4/x86_64-apple-darwin20/ggstatsplot/0.12.3/<hash>/ggstatsplot
```

That means many exact versions can still be recovered even when the old cache contents are gone.

## Build-Relevant Package Versions Recovered

These are the packages most immediately relevant to the current Quarto build and results chapter.

| Package | Recovered version | Evidence source | Notes |
| --- | --- | --- | --- |
| `here` | `1.0.1` | broken symlink target | old Intel cache path only |
| `modelsummary` | `2.1.0` | local `DESCRIPTION` | built under `R 4.4.0` on 2024-05-20 |
| `tinytable` | `0.3.0` | local `DESCRIPTION` | built under `R 4.4.0` on 2024-05-18 |
| `ggstatsplot` | `0.12.3` | broken symlink target | old Intel cache path only |
| `ggpubr` | `0.6.0` | broken symlink target | old Intel cache path only |
| `ggsci` | `3.1.0` | local `DESCRIPTION` | built under `R 4.4.0` on 2024-05-22 |
| `rstatix` | `0.7.2` | broken symlink target | old Intel cache path only |
| `DHARMa` | `0.4.6` | broken symlink target | old Intel cache path only |
| `car` | `3.1-2` | broken symlink target | old Intel cache path only |
| `pscl` | `1.5.9` | broken symlink target | old Intel cache path only |
| `coin` | `1.4-3` | broken symlink target | old Intel cache path only |
| `irr` | `0.84.1` | broken symlink target | old Intel cache path only |
| `tictoc` | `1.2.1` | broken symlink target | old Intel cache path only |
| `PMCMRplus` | `1.9.10` | broken symlink target | old Intel cache path only |
| `moments` | `0.14.1` | broken symlink target | old Intel cache path only |
| `janitor` | `2.2.0` | broken symlink target | old Intel cache path only |
| `lme4` | `1.1-35.3` | broken symlink target | old Intel cache path only |
| `lmerTest` | `3.1-3` | broken symlink target | old Intel cache path only |
| `emmeans` | `1.10.2` | local `DESCRIPTION` | built under `R 4.4.0` on 2024-05-21 |
| `performance` | `0.11.0` | broken symlink target | matches `renv.lock` |
| `insight` | `0.19.11` | local `DESCRIPTION` | one patch newer than `renv.lock` |
| `parameters` | `0.21.7` | local `DESCRIPTION` | one patch newer than `renv.lock` |
| `effectsize` | `0.8.8` | local `DESCRIPTION` | one patch newer than `renv.lock` |
| `bayestestR` | `0.13.2` | broken symlink target | matches `renv.lock` |
| `datawizard` | `0.10.0` | broken symlink target | matches `renv.lock` |
| `afex` | `1.3-1` | broken symlink target | old Intel cache path only |
| `BayesFactor` | `0.9.12-4.7` | broken symlink target | old Intel cache path only |
| `abind` | `1.4-5` | broken symlink target | old Intel cache path only |
| `ape` | `5.8` | broken symlink target | old Intel cache path only |

## How To Interpret This

- A local `DESCRIPTION` file is the strongest evidence. It gives both the exact version and the package `Built:` metadata.
- A broken symlink target is still strong version evidence, but it does not preserve package contents or build metadata.
- This Intel library cannot be used directly by native arm64 R. It is historical evidence, not a drop-in runtime for the current machine.
- The Intel library complements `renv.lock`; it does not replace it.

## Most Important Differences From `renv.lock`

The following build-relevant packages appear in the preserved Intel library but are missing from [`renv.lock`](/Volumes/Casa/dev/dissertation/renv.lock):

- `here`
- `modelsummary`
- `tinytable`
- `ggstatsplot`
- `ggpubr`
- `rstatix`
- `DHARMa`
- `car`
- `pscl`
- `irr`
- `tictoc`
- `PMCMRplus`
- `moments`
- `janitor`
- `lme4`
- `lmerTest`
- `afex`
- `BayesFactor`
- `abind`
- `ape`

The following easystats-family versions differ slightly between the preserved Intel library and `renv.lock`:

| Package | Intel library | `renv.lock` |
| --- | --- | --- |
| `insight` | `0.19.11` | `0.19.10` |
| `parameters` | `0.21.7` | `0.21.6` |
| `effectsize` | `0.8.8` | `0.8.7` |

## Practical Use

This manifest is useful for:

- choosing historically plausible package versions when the current build fails
- deciding which packages should be added to the eventual archival lockfile
- documenting why a pure `renv::restore()` was not sufficient on the new machine

The next logical use of this manifest is to guide targeted pinning for the current blockers, starting with packages implicated by the latest build failures:

- `modelsummary 2.1.0`
- `tinytable 0.3.0`
- `ggstatsplot 0.12.3`

## Regeneration Notes

This manifest was derived by inspecting package directories and broken symlink targets under the Intel library root. A direct package directory preserves `DESCRIPTION`; a broken symlink preserves only the cache path, from which the version can still be inferred.

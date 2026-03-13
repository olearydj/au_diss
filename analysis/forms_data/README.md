# forms_data

This directory holds the active R-side data-curation notebook for the dissertation and its local QA outputs.

## Role

- `forms_data.Rmd` reads preserved source/curation inputs from `data/source/` plus the timing handoff artifact `data/csv/i1_times_v2.csv`
- it cleans and joins those inputs
- it writes local QA/debug CSVs to `output/`
- it writes the main curated workbook to `data/combined_results.xlsx`

## Pipeline Position

This notebook is downstream of the Python extraction layer in `parse_xml/` and upstream of the manuscript analysis chapters.

In practical terms:

1. `parse_xml/process_data.py` uses the external participant/XML archive plus notes/workbook data to produce `data/reports/` and `data/csv/i1_times_v2.csv`
2. `forms_data.Rmd` curates those preserved artifacts into `data/combined_results.xlsx`
3. the manuscript analysis reads `data/combined_results.xlsx` and supporting `rdata/*.RData`

## Boundary

This folder is intentionally not under `archive/` because the curation step is still part of the active provenance story.

The longer-term structural idea, if a broader refactor is worth doing later, is:

- keep active R curation under `analysis/`
- keep the upstream XML/video extractor separate from that analysis layer
- if the repo later gets a broader pipeline namespace, move the Python extractor under that higher-level grouping rather than collapsing it into this folder

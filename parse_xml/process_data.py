"""process data, generate timing csv and combined participant reports"""

import csv
import glob
import logging
import os
from pathlib import Path

import typer
from rich import inspect
from rich import print as rprint
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

install(show_locals=True)  # rich tracebacks

REPORT_DIR = "/Users/djo/dev/au/au_diss/reports/"


def init_logging():
    """
    Initializes a logger with a RichHandler for rich, colorful logging output.

    This function sets up the logging module to log messages at the INFO level,
    with a specific format and date format. The RichHandler is configured to
    not highlight any parts of the log messages automatically.

    Returns:
        logging.Logger: A logger instance configured for use throughout the application.
    """
    console = Console()

    handler = RichHandler(console=console)
    handler.highlighter = None

    # Setup the logging module to use the RichHandler
    logging.basicConfig(
        level="INFO", format="%(message)s", datefmt="[%X]", handlers=[handler]
    )

    # override logging for packages
    logging.getLogger("gensim").setLevel(logging.WARNING)

    # return the logger object for global use
    return logging.getLogger("rich")


def extract_comments(md_file_path):
    """
    Extracts the h2 elements and underlying comments from hand-transcribed
    markdown notes (i.e., 1???.md). Ensures all notes are prefixed with "- ",
    and all h2 elements are preceded by one blank line.

    Args:
        md_file_path (Path): Path to the markdown file to extract comments from.

    Returns:
        md_out (list[str]): Processed lines.
    """
    logger.info(f"*** Extracting comments from: {md_file_path}")

    with open(md_file_path, "r") as md_input:
        md_in = md_input.readlines()

    h2 = False
    md_out = []

    for line in md_in:
        if line.startswith("##"):
            h2 = True
        elif line.isspace():
            h2 = False
        if h2:
            if not line.startswith(("- ", "##")):
                # fix notes that aren't bulleted
                line = "- " + line
            if line.startswith("##"):
                line = "\n#" + line
            md_out.append(line)
            # print(line, end="")

    # rprint(md_out)
    return md_out


def main(REPORT_DIR: str = REPORT_DIR):
    logger.info("-- Entering main...")
    report_path = Path(REPORT_DIR)

    # for each report
    reports = sorted(report_path.glob("????.md"))
    logger.info(f"> Processing {len(reports)} reports...")

    for report in reports:
        # e.g. if report = /Users/djo/dev/au/au_diss/reports/1001.md
        report_num = report.stem  # 1001
        report_dir = report.parent.name  # reports
        md_file = report.name  # 1001.md
        # md_file_path = str(report)  # /Users/djo/dev/au/au_diss/reports/1001.md

        # extract script comments and feedback from hand-transcribed trial notes
        trial_notes = extract_comments(report)

    # extract data from xml
    # save csv (xls?)
    # generate md reports, incorporating data from csv


if __name__ == "__main__":
    # set up logging
    logger = init_logging()
    logger.info("-- Logging setup complete.")

    typer.run(main)

"""
- generate_combined_reports: main entry point
    - main: combines md comments and extracted XML to generate report and csv
    - extract_comments: extracts hand-written comments from markdown files
- parse_xml: called by generate_combined_reports
    - convert_to_seconds: converts kyno timestamps into seconds
    - generate_markdown_report: extracts data from XML files, generates markdown report data
- process_video_tree: early attempt at report generation wrapper
    - first attempt at a report generation wrapper
    - searches dir tree, finds xmls files, calls generate_markdown_report, and writes that report
"""

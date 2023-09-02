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


def main(REPORT_DIR: str = REPORT_DIR):
    logger.info("-- Entering main.")

    # for each report
    reports = sorted(glob.glob(os.path.join(REPORT_DIR, "????.md")))
    logger.info(f"> Processing {len(reports)} reports...")

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

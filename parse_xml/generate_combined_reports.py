# parse all 1???.md files and generate combined report

import glob
import os
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown
from parse_xml import convert_to_seconds
from parse_xml import generate_markdown_report

install()  # install rich traceback handler
console = Console(highlight=False)


def main(reports, verbose=True):
    """build combined reports for the specified files and root dir"""
    for report in reports:
        report_num, ext = os.path.splitext(os.path.basename(report))
        report_dir = report.split("/")[-2]
        md_file = report_num + ext
        md_file_path = report

        try:
            # extract comments from general observations & feedback
            console.print(
                f"\n:gear: [bold green]running:[/] :pencil:[royal_blue1]{md_file}[/] in :open_file_folder:[blue_violet]{report_dir}[/]"
            )
            comments = extract_comments(md_file_path)
            combined_report = ""

            # extract data from xml files - video logs
            for phase in ["Learn", "Recall"]:
                xml_file = f"{report_num}-{phase}.xml"

                # glob returns a list of matching dirs, assume first is correct
                data_dir = glob.glob(os.path.join(DATA_ROOT_DIR, f"{report_num}-*"))[0]
                xml_path = os.path.join(data_dir, "videos", xml_file)
                console.print(f"\n[green]process [/]{xml_file} in {xml_path}")

                xml_report = generate_markdown_report(xml_path)
                combined_report = xml_report + "".join(comments)

                # print result to console
                if verbose:
                    if verbose == "md":
                        md = Markdown(combined_report)
                        console.print(md)
                    else:
                        for line in combined_report:
                            print(line, end="")

        except:
            console.print(
                f"\n:police_car_light: error on [bold red]{md_file}[/] :police_car_light:"
            )


def extract_comments(md_file_path):
    """
    Extracts the h2 elements and underlying comments from hand-transcribed
    markdown notes (i.e., 1???.md). Ensures all notes are prefixed with "- ",
    and all h2 elements are preceded by one blank line.

    Args:
        md_file_path (str): Path to the markdown file to extract comments from.

    Returns:
        md_out (list[str]): Processed lines.
    """
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
                line = "\n" + line
            md_out.append(line)
            # print(line, end="")

    return md_out


if __name__ == "__main__":
    REPORT_DIR = "/Users/djo/dev/au/au_diss/reports/"
    DATA_ROOT_DIR = "/Volumes/ThunderBay mini/Research Master/data/"
    report_files = sorted(glob.glob(os.path.join(REPORT_DIR, "????.md")))[:3]
    main(report_files)

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
    # print("*** in main\n")
    for report in reports:
        report_num, ext = os.path.splitext(os.path.basename(report))
        report_dir = report.split("/")[-2]
        md_file = report_num + ext
        md_file_path = report

        # print("*** ", report_num, report_dir, md_file_path, sep="   ")

        try:
            # extract comments from general observations & feedback
            console.print(
                f":gear: [bold green]running:[/] :pencil:[royal_blue1]{md_file}[/] in :open_file_folder:[blue_violet]{report_dir}[/]"
            )
            comments = extract_comments(md_file_path)

            # extract data from xml files - video logs
            for phase_num, phase_name in enumerate(["Learn", "Recall"], start=1):
                # print(f"*** building XML report for Phase {phase_num}: {phase_name}")
                report_header = (
                    f"# Trial {report_num}\n\n"
                    "## Participant Information\n\n"
                    "*Add information from xls demographics page, including treatment, date, etc.*\n\n"
                    "## General Notes\n"
                    f"{''.join(comments)}"
                )

                if phase_num == 1:
                    combined_report = report_header

                combined_report += f"\n## Phase {phase_num}: {'Learning' if phase_num == 1 else phase_name}\n\n"

                xml_file = f"{report_num}-{phase_name}.xml"
                # print(f"*** processing {xml_file}")

                # glob returns a list of matching dirs, assume first is correct
                data_dir = glob.glob(os.path.join(DATA_ROOT_DIR, f"{report_num}-*"))[0]
                xml_path = os.path.join(data_dir, "videos", xml_file)
                console.print(f"[green]process [/]{xml_file} in {xml_path}\n")

                # print(f"*** generating markdown report\n")
                xml_report = generate_markdown_report(xml_path)
                for sec_name, sec_data in xml_report.items():
                    # print(f"*** combining report: {sec_name}")
                    combined_report += sec_data

            # print result to console
            if verbose:
                if verbose == "md":
                    md = Markdown(combined_report)
                    console.print(md)
                else:
                    for line in combined_report:
                        print(line, end="")

        except Exception as e:
            console.print(
                f"\n:police_car_light: error on [bold red]{md_file}[/] :police_car_light:"
            )
            console.print_exception()


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
    # print("*** in extract_comments")
    # print(f"*** extracting comments from: {md_file_path}\n")

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

    # print("*** leaving extract_comments\n")
    return md_out


if __name__ == "__main__":
    REPORT_DIR = "/Users/djo/dev/au/au_diss/reports/"
    DATA_ROOT_DIR = "/Volumes/ThunderBay mini/Research Master/data/"
    report_files = sorted(glob.glob(os.path.join(REPORT_DIR, "????.md")))[:1]
    main(report_files)

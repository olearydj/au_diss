# parse all 1???.md files and generate combined report

import os
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown

install()  # install rich traceback handler
console = Console(highlight=False)


def main(root, first, last, verbose=False):
    """build combined reports for the specified files and root dir"""
    for p_num in range(first, last + 1):
        md_file = f"{p_num}.md"
        md_file_path = os.path.join(root, md_file)
        if os.path.isfile(md_file_path):
            console.print(
                f'\n:gear: [bold green]running:[/] :pencil:[royal_blue1]{md_file}[/] in :open_file_folder:[blue_violet]{root.split("/")[-2]}[/]'
            )
            comments = extract_comments(md_file_path)
            if verbose:
                if verbose == "md":
                    md = Markdown("\n".join(comments))
                    console.print(md)
                else:
                    for line in comments:
                        print(line, end="")
            console.print(f"\n[green]process [/]{p_num}-learn.md")
            console.print(f"[green]process [/]{p_num}-recall.md")
        else:
            console.print(
                f"\n:police_car_light: [bold red]{md_file} does not exist[/] :police_car_light:"
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
    dev_root = "/Users/djo/dev/au/au_diss/reports/"
    start, stop = 1001, 1006
    main(dev_root, start, stop)

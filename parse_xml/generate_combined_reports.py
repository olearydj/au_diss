# parse all 1???.md files and generate combined report

import os


def main(root, first, last):
    """build combined reports for the specified files and root dir"""
    for p_num in range(first, last + 1):
        md_file = f"{p_num}.md"
        md_file_path = os.path.join(root, md_file)
        if os.path.isfile(md_file_path):
            print(f'\n*** running: {md_file} in {root.split("/")[-2]}')
            extract_comments(md_file_path)
        else:
            print(f"\n*** {md_file} does not exist")


def extract_comments(md_file_path):
    """
    Extracts the h2 elements and underlying comments from hand-transcribed
    markdown notes (i.e., 1???.md). Ensures all notes are prefixed with "- ".

    Args:
        md_file_path (str): Path to the markdown file to extract comments from.

    Returns:
        list[str]: Items represent a line from the h2 sections of the MD file.
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
            md_out.append(line)
            print(line, end="")


if __name__ == "__main__":
    dev_root = "/Users/djo/dev/au/au_diss/reports/"
    start, stop = 1001, 1006
    main(dev_root, start, stop)

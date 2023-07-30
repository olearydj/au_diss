import os
import xml.etree.ElementTree as ET
from parse_xml import generate_markdown_report


def traverse_and_generate_reports(root_dir, output_dir, test=True):
    """
    Traverse a directory tree and generate markdown reports for each XML file found.

    The function searches for XML files within the specified root directory and its subdirectories.
    For each XML file found, it generates a markdown report using the `generate_markdown_report` function
    and writes the report to a file named `report.md` in the same directory as the XML file.

    Parameters:
    - root_directory (str): The path to the root directory to begin the traversal.
    - output_directory (str): subdirectory in root to put output files
    - test (bool): run in test mode (default) or not

    Returns:
    None

    Example:
    >>> traverse_and_generate_reports("/path/to/root/directory")
    Report generated for /path/to/root/directory/file1.xml at /path/to/root/directory/report.md
    Report generated for /path/to/root/directory/subdir/file2.xml at /path/to/root/directory/subdir/report.md
    ... and so on for each XML file found.
    """

    # Walk through each directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if file is an XML
            if filename.endswith(".xml"):
                xml_file_path = os.path.join(dirpath, filename)
                md_filename = filename.split(".")[0] + ".md"
                report_file_path = os.path.join(output_dir, md_filename)
                if not test:
                    try:
                        markdown_report = generate_markdown_report(xml_file_path)
                        with open(report_file_path, "w") as report_file:
                            report_file.write(markdown_report)
                        print(f"✅ {filename} → {report_file_path}")
                    except Exception as e:
                        print(f"❌ Error processing {xml_file_path}: {e}")
                else:
                    print(f"🧪 {filename} → {report_file_path}")


if __name__ == "__main__":
    dev_root = "/Users/djo/dev/au/au_diss/parse_xml"
    prod_root = "/Volumes/ThunderBay mini/Research Master/"
    out_dir = "/Users/djo/dev/au/au_diss/reports/"
    traverse_and_generate_reports(prod_root, out_dir, test=False)

import os
import xml.etree.ElementTree as ET

# [Include the convert_to_seconds() and generate_markdown_report() functions here]

def traverse_and_generate_reports(root_directory):
    # Walk through each directory
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            # Check if file is an XML
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(dirpath, filename)
                try:
                    markdown_report = generate_markdown_report(xml_file_path)
                    report_file_path = os.path.join(dirpath, 'report.md')
                    with open(report_file_path, 'w') as report_file:
                        report_file.write(markdown_report)
                    print(f"Report generated for {xml_file_path} at {report_file_path}")
                except Exception as e:
                    print(f"Error processing {xml_file_path}: {e}")

# Example Usage:
# traverse_and_generate_reports("/path/to/root/directory")

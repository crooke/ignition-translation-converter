import xml.etree.cElementTree as ET
import csv

def convert(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    with open(output_file, 'w+', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file)

        # First element in root is the Locale info
        locale = root[0].text
        writer.writerow([locale])

        # Write a header
        writer.writerow([])
        writer.writerow(["Term", "Translation"])

        # Every element after should be a term-translation pair
        for child in root[1:]:
            term = child.attrib.get('key')
            translation = child.text if child.text else ''
            writer.writerow([term, translation])

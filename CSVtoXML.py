from lxml import etree as ET
import csv

def convert(input_file, output_file):
    # Get our XML structure ready
    root = ET.Element('properties')
    tree = ET.ElementTree(root)
    doctype = '<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">'

    # Parse the CSV file and build the XML
    with open(input_file, newline='') as csv_file:
        reader = csv.reader(csv_file)

        # First row is the Local info
        locale = next(reader)[0]
        ET.SubElement(root, 'comment').text = locale

        # Skip the next two rows (better way of doing this?)
        next(reader) #Blank row
        next(reader) #Header row

        # Fourth row on should consist of term-translation pairs
        for row in reader:
            term = row[0]
            translation = row[1]
            ET.SubElement(root, 'entry', key=term).text = translation


    tree.write(output_file, encoding='UTF-8', xml_declaration=True, pretty_print=True, doctype=doctype)
import argparse
from os.path import exists
import XMLtoCSV, CSVtoXML

# Define command-line arguments
program_description = "Converts Ignition's translation database XML file to a CSV file and vice-versa."
parser = argparse.ArgumentParser(description=program_description)
parser.add_argument('input_file', type=str, help='Path to the file to convert')
parser.add_argument('output_file', type=str, help='Path to the file to output')

args = parser.parse_args()

if not exists(args.input_file):
    print("Input file doesn't exist.")
    exit(1)

# TODO: Create more robust way of checking whether we should convert from XML to CSV or vice-versa
if args.input_file.endswith(('xml','XML')):
    XMLtoCSV.convert(args.input_file, args.output_file)
    print("Successfully converted translation database from XML to CSV")

elif args.input_file.endswith(('csv','CSV')):
    CSVtoXML.convert(args.input_file, args.output_file)
    print("Successfully converted translation database from CSV to XML")

else:
    print("Unrecognized input file: %s" % args.input_file)
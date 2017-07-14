# Ignition Translation Converter

Inductive Automation's Ignition designer lets you export terms from the translation database in XML format. This command-line program written in Python is a simple tool that allows you to convert the XML file to CSV for easier editing in a spreadsheet program like LibreOffice Calc or MS Excel, as well as converting the CSV back to XML for importing the translated terms into your Ignition project.

## Requirements

The program was built using Python3 standard libraries in addition to the [lxml](http://lxml.de/) library for XML processing, which you can easily get with `pip install lxml`.

## Usage

Running `python main.py -h` from the command-line should provide some help:

```sh
usage: main.py [-h] input_file output_file

Converts Ignition's translation database XML file to a CSV file and vice-
versa.

positional arguments:
  input_file   Path to the file to convert
  output_file  Path to the file to output

optional arguments:
  -h, --help   show this help message and exit
```

Presumably, you'd start by converting the XML file you exported from Ignition to CSV:

```sh
python main.py '/home/user/TranslationTerms.xml' '/home/user/TranslationTerms.csv'
```

Once you've translated all your terms, convert it back to XML:

```sh
python main.py '/home/user/TranslationTerms.csv' 'home/user/TranslationTerms.xml'
```

Import back into Ignition and enjoy!

Feel free to submit an issue or contribute to the tool.
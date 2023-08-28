#!/usr/bin/env python3
# text_files_to_spreadsheet.py — An exercise in manipulating Excel files.
# For more information, see README.md

from pathlib import Path
import logging
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)

logging.disable(logging.CRITICAL)  # Note out to enable logging.


def main():
    """Executes prior functions in sequence."""
    doc_list = find_files()
    doc_contents = pull_contents(doc_list)
    logging.debug(doc_contents)
    write_excel(doc_contents)


def find_files():
    """Find all txt files in designated folder
    and make a list of their file paths."""
    return list(Path(input("Please type file path here: ")).glob("*.txt"))


def pull_contents(file_list):
    """Convert contents of each line of each text file into a list of lists."""
    document_contents = []
    for item in file_list:
        with open(item, "rb") as file_contents:
            document_contents.append(file_contents.readlines())
    return document_contents


def write_excel(contents):
    """Create an Excel file with every txt files as its own column
    and each line of the txt file as a row."""
    wb = Workbook()
    sheet = wb.active

    for i, _ in enumerate(contents):
        for j, _ in enumerate(contents[i]):
            sheet[f"{get_column_letter(i + 1)}{j + 1}"] = contents[i][j]

    wb.save("text_to_spread.xlsx")


if __name__ == "__main__":
    main()

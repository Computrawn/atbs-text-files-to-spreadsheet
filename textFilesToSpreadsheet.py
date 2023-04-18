#! python3
# textFilesToSpreadsheet.py — An exercise in manipulating Excel files.
# For more information, see project_details.txt.

from pathlib import Path
import logging
import openpyxl

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL) # Remove notation to disable logging.


def find_files():
    """Find all txt files in designated folder."""
    user_path = Path(input("Please type file path here: "))
    document_list = list(user_path.glob("*.txt"))
    logging.debug(document_list)
    return document_list


def pull_contents(file_list):
    """Convert contents of each line of each text file into a list of lists."""
    document_contents = []
    for file in file_list:
        with open(file, "rb") as f:
            lines = f.readlines()
            document_contents.append(lines)
    return document_contents


doc_list = find_files()
doc_contents = pull_contents(doc_list)
logging.debug(doc_contents)

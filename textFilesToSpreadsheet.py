#! python3
# textFilesToSpreadsheet.py — An exercise in manipulating Excel files.
# For more information, see project_details.txt.

import os
import openpyxl

import logging

logging.basicConfig(level=logging.DEBUG, filename="logging.txt")

document_contents = []


def find_files():
    user_input = input("Please type file path here: ")
    directory = os.chdir(user_input)
    document_list = os.listdir(directory)
    text_files = []
    for item in document_list:
        text_files.append(f"{user_input}/{item}")
    return text_files


def pull_contents(doc_list):
    for file in doc_list:
        with open(file, "rb") as f:
            lines = f.readlines()
            document_contents.append(lines)


document_list = find_files()
pull_contents(document_list)
logging.debug(document_contents)

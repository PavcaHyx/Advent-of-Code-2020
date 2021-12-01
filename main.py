import re
from pathlib import Path


def file_to_open(name_of_file):
    input_folder = Path("inputs/")
    return input_folder / name_of_file
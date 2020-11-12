"""
This file manages basic functions for the program.

To do:
* diff_list(): implement a case_sensitive: bool = True with a inlist() bool function which can be case-insensitive for the 'if item_1 not in list_2' part
"""
#   IMPORTING THIRD-PARTY LIBRARIES
import os
import datetime

#   IMPORTING PROJECT FILES
import preferences as Pref

#   DEFINING FILE-WIDE VARIABLES
# -



def count_indent(line: str, indent_marker: str = '\t') -> int:
    """
    This function counts the indentation level of a given string.
    :param line: The line to count the indentation level for
    :param indent_marker: Indent marker (optional)
    :return: The indentation level of the line
    """
    indent_len = len(indent_marker)
    indent = 0
    while line and line[:indent_len] == indent_marker:
        indent += 1
        line = line[indent_len:]
    return indent



def replace_char(line:str, char: str, replacement: str = '') -> str:
    while char in line:
        line = line.replace(char, replacement)
    return line



def replace_chars(line: str, chars_dict: dict) -> str:
    for char_to_replace in chars_dict:
        line = replace_char(line, char_to_replace, chars_dict[char_to_replace])
    return line



def remove_chars(line: str, *chars: str) -> str:
    for char_to_remove in chars:
        line = replace_char(line, char_to_remove)
    return line



def remove_on_edges(line: str, *chars: str) -> str:
    for char_to_remove in chars:
        while line[0] == char_to_remove:
            line = line[1:]
        while line[-1] == char_to_remove:
            line = line[:-1]
    return line



def format_dir_path(dir_path: str):
    _psep_ = Pref._psep_
    if dir_path[-1] != _psep_:
        dir_path += _psep_
    return dir_path


def split_filepath(filepath: str) -> (str, str):
    _psep_ = Pref._psep_
    filepath_split = filepath.split(_psep_)

    dirpath = _psep_.join(filepath_split[:-1])
    filename = filepath_split[-1]

    return dirpath, filename


def split_filename(filename: str) -> (str, str):
    _esep_ = Pref._esep_
    filename_split = filename.split(_esep_)

    name = _esep_.join(filename_split[:-1])
    extension = filename_split[-1]

    return name, extension


def get_date_formatted(filepath: str) -> str:
    birthtime = os.stat(filepath).st_birthtime
    birthtime_formatted = datetime.datetime.fromtimestamp(birthtime).strftime('%Y%m%d-%H%M%S')
    return birthtime_formatted



#
def diff_list(list_1: list, list_2: list) -> (list, list):

    list_removed = [item_1 for item_1 in list_1 if item_1 not in list_2]
    list_added   = [item_2 for item_2 in list_2 if item_2 not in list_1]

    return list_added, list_removed



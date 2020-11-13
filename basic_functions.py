"""
This file manages basic functions for the program.

To do:
* diff_list(): implement a case_sensitive: bool = True with a inlist() bool function which can be case-insensitive for the 'if item_1 not in list_2' part
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import os
import datetime
import subprocess

#   IMPORTING PROJECT FILES
import preferences as Pref

#   DEFINING FILE-WIDE VARIABLES
_psep_ = Pref._psep_




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
    """
    This function replaces a character into another in a string.
    :param line: The string to replace the character in
    :param char: The character to replace
    :param replacement: The replacement character
    :return: The processed string
    """
    while char in line:
        line = line.replace(char, replacement)

    return line




def replace_chars(line: str, chars_dict: dict) -> str:
    """
    This function replaces characters into other characters in a string.
    :param line: The string to replace the characters in
    :param chars_dict: The dictionary of characters to replace and their replacement character
    :return: The processed string
    """
    for char_to_replace in chars_dict:
        line = replace_char(line, char_to_replace, chars_dict[char_to_replace])

    return line




def remove_chars(line: str, *chars: str) -> str:
    """
    This function removes characters from a string.
    :param line: The string to remove the characters in
    :param chars: The characters to remove
    :return: The processed string
    """
    for char_to_remove in chars:
        line = replace_char(line, char_to_remove)

    return line




def remove_on_edges(line: str, *chars: str) -> str:
    """
    This function removes characters from the edges of a string
    :param line: The string to remove the characters in
    :param chars: The characters to remove
    :return: The processed string
    """
    for char_to_remove in chars:

        #   1. Removing in leading position
        while line[0] == char_to_remove:
            line = line[1:]

        #   2. Removing in trailing position
        while line[-1] == char_to_remove:
            line = line[:-1]

    return line




def format_dir_path(dirpath: str):
    """
    This function makes sure that a directory's path always ends in a path separator.
    :param dirpath: The directory's initial path
    :return: The directory's processed path
    """
    if dirpath[-1] != _psep_:
        dirpath += _psep_

    return dirpath




def split_filepath(filepath: str) -> (str, str):
    """
    This function splits a file's path into its parent directory's path and its name.
    :param filepath: The file's path
    :return: The file's parent directory's path and the file's name (with extension)
    """
    filepath_split = filepath.split(_psep_)

    dirpath = _psep_.join(filepath_split[:-1])
    filename = filepath_split[-1]

    dirpath = format_dir_path(dirpath)

    return dirpath, filename




def split_filename(filename: str) -> (str, str):
    """
    This function splits a file's full name into its name and its extension.
    :param filename: The file's full name
    :return: The file's name and the file's extension
    """
    _esep_ = Pref._esep_
    filename_split = filename.split(_esep_)

    name = _esep_.join(filename_split[:-1])
    extension = filename_split[-1]

    return name, extension




def get_birthtime_formatted(filepath: str) -> str:
    """
    This function gets the birthtime of a file as a formatted '%Y%m%d-%H%M%S' string.
    :param filepath: The path of the file
    :return: The formatted birthtime string
    """
    birthtime = os.stat(filepath).st_birthtime
    birthtime_formatted = datetime.datetime.fromtimestamp(birthtime).strftime('%Y%m%d-%H%M%S')
    return birthtime_formatted




def diff_list(list_1: list, list_2: list) -> (list, list):
    """
    This function compares two lists and generates a list of items removed and a list of items added between the initial and altered lists.
    :param list_1: The initial list
    :param list_2: The altered list
    :return: The list of removed items and the list of added items (in this order)
    """
    list_removed = [item_1 for item_1 in list_1 if item_1 not in list_2]
    list_added   = [item_2 for item_2 in list_2 if item_2 not in list_1]

    return list_removed, list_added




def ishidden(filename: str) -> bool:
    """
    This function checks if a file is hidden by default (in the macOS file system).
    :param filename: The name of the file to check for
    :return: The hidden status of the file
    """
    return filename[0] == '.'




def size_bytes(path: str) -> int:
    """
    This function get the total size of a path in bytes.
    :param path: The path to analyse
    :return: The size of the path (in bytes)
    """

    #   1. Generating the command
    cmd = ['find',
           path,
           '-type f -exec ls -l {} \; | awk \'{sum += $5} END {print sum}\''
           ]

    #   2. Running the command
    output_bytes = subprocess.check_output([' '.join(cmd)], shell=True)

    return int( output_bytes.decode('utf-8')[:-1] )




def display_progression(filecount: int, total_filecount: int, display_every: int):
    """
    This function display the progression of filecount towards total_filecount in steps of display_every.
    :param filecount: The progressing file count
    :param total_filecount: The total file count
    :param display_every: The steps for displaying the progress
    :return:
    """

    if filecount % display_every == 0 or filecount == total_filecount:

        percentage = round(filecount / total_filecount * 100, 1)

        message = f'{percentage}% done'
        print(message)
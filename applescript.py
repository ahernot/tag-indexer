"""
This file handles UNIX alias generation using an AppleScript command run through the Bash terminal.
Partially adapted from: https://apple.stackexchange.com/questions/278117/how-to-use-applescript-in-a-bash-script-to-create-an-alias-for-an-app
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import os

#   IMPORTING PROJECT FILES
import basic_functions as BFunc

#   DEFINING FILE-WIDE VARIABLES
# -


def make_alias(parent_path: str, child_path: str):
    """
    This function creates an Unix alias of a file, using an AppleScript command run through macOS' terminal.
    :param parent_path: The path of the file to alias
    :param child_path: The path of the alias to create (output)
    :return:
    """

    #   1. Extracting the alias target directory
    child_dir, child_name = BFunc.split_filepath(child_path)

    #   2. Making the alias target directory if it doesn't exist
    try:
        os.makedirs(child_dir)
    except:
        pass

    #   3. Generating the alias file
    #   3.1. Generating the command
    applescript_command = f'set filePath to "{parent_path}"\n' \
                          f'set endPath to "{child_dir}"\n' \
                          f'tell application "Finder"\n' \
                          f'make new alias to POSIX file filePath at POSIX file endPath\n' \
                          f'set name of result to "{child_name}"\n' \
                          f'end tell'

    os_command = f'osascript -e \'{applescript_command}\''

    #   3.2. Running the command
    os.popen(os_command)

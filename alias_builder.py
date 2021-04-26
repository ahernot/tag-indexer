"""
This file handles UNIX alias generation using an AppleScript command run through the Bash terminal.
Partially adapted from: https://apple.stackexchange.com/questions/278117/how-to-use-applescript-in-a-bash-script-to-create-an-alias-for-an-app
"""

import os


def make_alias (filepath: str, alias_dirpath: str, alias_name: str):
    """
    This function creates an Unix alias of a file, using an AppleScript command run through macOS' terminal.
    :param parent_path: The path of the file to alias
    :param child_path: The path of the alias to create (output)
    :return:
    """

    if not os.path.exists (filepath) or not os.path.exists (alias_dirpath):
        raise FileNotFoundError

    applescript_command = \
        f'set filePath to "{filepath}"\n' \
        f'set aliasPath to "{alias_dirpath}"\n' \
        f'tell application "Finder"\n' \
        f'make new alias to POSIX file filePath at POSIX file aliasPath\n' \
        f'set name of result to "{alias_name}"\n' \
        f'end tell'

    os_command = f'osascript -e \'{applescript_command}\''

    os.popen(os_command)

#!/usr/bin/env python3

import os


def make_alias (filepath: str, alias_dirpath: str, alias_name: str):
    """
    Create a Unix alias of filepath: AppleScript command run through macOS command line
    Partially adapted from https://apple.stackexchange.com/questions/278117/how-to-use-applescript-in-a-bash-script-to-create-an-alias-for-an-app
    :param parent_path: original filepath
    :param child_path: alias dirpath
    :param alias_name: alias name
    :return: path of the created alias file
    """

    # Build alias path
    alias_path = os.path.join (alias_dirpath, alias_name)

    # Exceptions
    if not os.path.exists (filepath) or not os.path.exists (alias_dirpath) or os.path.exists (alias_path):
        raise FileNotFoundError

    # Generate command
    applescript_command = \
        f'set filePath to "{filepath}"\n' \
        f'set aliasPath to "{alias_dirpath}"\n' \
        f'tell application "Finder"\n' \
        f'make new alias to POSIX file filePath at POSIX file aliasPath\n' \
        f'set name of result to "{alias_name}"\n' \
        f'end tell'
    os_command = f'osascript -e \'{applescript_command}\''

    # Run command
    os.popen (os_command)

    return alias_path

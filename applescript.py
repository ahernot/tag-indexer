import os

def make_alias(parent_path: str, child_path: str):
    """
    This function creates an Unix alias of a file, using an AppleScript command run through macOS' terminal.
    :param parent_path: The path of the file to alias
    :param child_path: The path of the alias to create (output)
    :return:
    """

    applescript_command = f'set filePath to "{parent_path}"\n' \
                          f'set endPath to "{child_path}"' \
                          f'\ntell application "Finder"\n' \
                          f'make new alias to POSIX file filePath at POSIX file endPath\n' \
                          f'end tell'

    os_command = f'osascript -e \'{applescript_command}\''

    os.system(os_command)

import os

def make_alias(parent_path: str, child_path: str):

    applescript_command = f'set filePath to "{parent_path}"\n' \
                          f'set endPath to "{child_path}"' \
                          f'\ntell application "Finder"\n' \
                          f'make new alias to POSIX file filePath at POSIX file endPath\n' \
                          f'end tell'

    os_command = f'osascript -e \'{applescript_command}\''

    os.system(os_command)

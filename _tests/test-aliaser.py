import os

parent_path = '/Users/anatole/Downloads/_TEST_PYTAGS_/DIR1/IMG_1934.JPG'
child_dir = '/Users/anatole/Documents/GitHub/tag-indexer/TEST_TARGET'

child_name = 'alias-PY'

applescript_command = \
    f'set filePath to "{parent_path}"\n' \
    f'set endPath to "{child_dir}"\n' \
    f'tell application "Finder"\n' \
    f'make new alias to POSIX file filePath at POSIX file endPath\n' \
    f'set name of result to "{child_name}"\n' \
    f'end tell'

os_command = f'osascript -e \'{applescript_command}\''

#   3.2. Running the command
os.popen(os_command)
"""
This files manages importing the program's preferences from the preferences.txt file.
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import os

#   IMPORTING PROJECT FILES
# -

#   DEFINING FILE-WIDE VARIABLES
main_path = os.path.realpath(__file__).replace('preferences.py', '')



# dir_to_process = ''
dir_to_process = '/Users/Anatole/Documents/TEST-directory-branching'
alias_dir = '/Users/Anatole/Documents/ALIAS'


ETA_calculation = True

_files_ = '_files_'

_dsep_ = '\t' # data separator
_lsep_ = '\n' # line separator
_psep_ = '/' # path separator
_esep_ = '.' # extension separator
_tsep_ = ', ' # tags list separator
_ssep_ = ' ' # space separator

tag_placeholder = '%'

database_name = 'database.txt' # relative database path

beacon_tags_name = '.pytags_tags'
beacon_sizes_name = '.pytags_sizes'
"""
This files manages importing the program's preferences from the preferences.txt file.
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import os

#   IMPORTING PROJECT FILES
# -

#   DEFINING FILE-WIDE VARIABLES
main_path = os.path.realpath(__file__).replace('preferences.py', '')
preferences_path = main_path + 'preferences.txt'

_files_ = '_files_'

_dbsep_ = '\t' # database separator
_dsep_ = '\t' # data separator
_lsep_ = '\n' # line separator
_psep_ = '/' # path separator
_esep_ = '.' # extension separator
_tsep_ = ', ' # tags list separator
_ssep_ = ' ' # space separator




def read() -> dict:
    """
    This function reads the program's preferences file and returns a comprehensive dictionary of the preferences.
    :return: The dictionary of preferences
    """

    #   0. Initialising the preferences dictionary
    preferences_dict = dict()

    #   1. Opening the preferences file
    try:
        with open(preferences_path, 'r', encoding='utf-8') as preferences_file:
            preferences_lines = preferences_file.readlines()

    except:
        raise FileNotFoundError(f'Unable to found the preferences.txt file in path \'{preferences_path}\'.')

    #   2. Processing the preferences
    for line in preferences_lines:

        #   2.1. Processing the line to remove line breaks (cannot use basic_functions.py since it calls preferences.py)
        while '\n' in line:
            line = line.replace('\n', '')

        #   2.2. Skipping empty lines
        if not line: continue

        #   2.3. Processing the line
        line_broken = line.split(_dbsep_)

        #   2.4. Adding the line to the preferences dictionary
        preferences_dict[line_broken[0]] = _dbsep_.join(line_broken[1:])


    return preferences_dict




#   Running the preferences reader
preferences_dict = read()




#   Generating the needed variables
dir_to_process = preferences_dict['dir_to_process']
alias_dir = preferences_dict['alias_dir']
tag_placeholder = preferences_dict['tag_placeholder']
database_name = preferences_dict['database_name'] # relative database path
beacon_tags_name = preferences_dict['beacon_tags_name']
beacon_sizes_name = preferences_dict['beacon_sizes_name']
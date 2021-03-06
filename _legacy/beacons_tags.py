"""
This file manages file tags hidden beacon files in directories.
"""

#   IMPORTING THIRD-PARTY LIBRARIES
# -

#   IMPORTING PROJECT FILES
import basic_functions as BFunc
import file_analysis as FFunc
import preferences as Pref

#   DEFINING FILE-WIDE VARIABLES
_lsep_ = Pref._lsep_
_dsep_ = Pref._dsep_
_tsep_ = Pref._tsep_
beacon_name = Pref.beacon_tags_name



def read_beacon(dirpath: str) -> dict:
    """
    This functions reads a beacon file and returns a dictionary containing its contents.
    :param dirpath: The path of the directory to read the beacon file from
    :return: The beacon file's dictionary
    """

    #   0. Generating the output dictionary
    beacon_dict = dict()

    #   1. Formatting the directory path (making sure that a path separator is present at the end)
    dirpath = BFunc.format_dir_path(dirpath)

    #   2. Opening the beacon file
    try:
        beacon = open(f'{dirpath}/{beacon_name}', 'r', encoding='utf-8')
    except: return beacon_dict

    #   3. Reading the beacon file's lines
    beacon_lines = beacon.readlines()
    beacon.close()

    #   4. Processing the beacon file's lines
    for line in beacon_lines:

        #   4.1. Removing line breaks
        line = BFunc.remove_chars(line, _lsep_)
        if not line: continue

        #   4.2. Splitting along the data separator
        line_split = line.split(_dsep_)
        if len(line_split) != 2: continue

        #   4.3. Unpacking
        childpath, child_tags = line_split

        #   4.4. Generating the tags list (empty string lists become empty lists)
        tags_list = child_tags.split(_tsep_)
        if tags_list == ['']: tags_list = list()

        #   4.5. Writing to the output dictionary
        beacon_dict[childpath] = tags_list

    return beacon_dict




def write_beacon(dirpath: str, children_paths: list, filename: str = beacon_name) -> str:
    """
    This function generates a hidden beacon file in a directory, logging its children's paths and sizes. It will overwrite any previously generated beacons.
    :param dirpath: The path of the directory to generate the beacon in
    :param children_paths: The paths of the files to save in the beacon
    :param filename: The name of the beacon (optional)
    :return: The path of the generated beacon
    """

    #   1. Formatting the directory path (making sure that a path separator is present at the end)
    dirpath = BFunc.format_dir_path(dirpath)

    #   2. Generating the beacon file's path
    beaconpath = f'{dirpath}{filename}'

    #   3. Opening the beacon file for writing
    with open(beaconpath, 'w', encoding='utf-8') as beacon:

        for childpath in children_paths:

            #   3.1. Calculating the size of the child file or directory
            tags_list = FFunc.get_tags(childpath)
            tags_str  = _tsep_.join(tags_list)

            #   3.2. Generating the line
            line = f'{childpath}{_dsep_}{tags_str}{_lsep_}'

            #   3.3. Writing to the file
            beacon.write(line)

    return beaconpath




def get_removed_files(children_paths: list, beacon_dict: dict) -> dict:
    """
    This function returns all the keys which are present in the beacon file but not in the provided list of files.
    :param children_paths: The list of filepaths
    :param beacon_dict: The generated beacon dictionary for the parent folder
    :return: The dictionary of removed files and their tags (according to the beacon_dict dictionary)
    """
    removed_dict = dict()

    for filepath in beacon_dict.keys():
        if filepath not in children_paths:
            removed_dict[filepath] = beacon_dict[filepath].copy()

    return removed_dict


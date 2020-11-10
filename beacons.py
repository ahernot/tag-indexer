# defaults write com.apple.finder AppleShowAllFiles YES


import basic_functions as BFunc
import indexing_functions as IFunc
import preferences as Pref


_lsep_ = Pref._lsep_
_dsep_ = Pref._dsep_
beacon_name = '.pytags'



def read_beacon(dirpath: str) -> dict:
    """
    This functions reads a beacon file and returns a dictionary containing its contents.
    :param dirpath: The path of the directory to read the beacon file from
    :return: The beacon file's dictionary
    """

    #   0. Generating the output dictionary
    beacon_dict = dict()

    #   1. Formatting the directory path (adding the final '/')
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
        childpath, child_size = line_split

        #   4.4. Writing to the output dictionary
        beacon_dict[childpath] = int(child_size)

    return beacon_dict




def write_beacon(dirpath: str, children_paths: list, filename: str = beacon_name) -> str:
    """
    This function generates a hidden beacon file in a directory, logging its children's paths and sizes. It will overwrite any previously generated beacons.
    :param dirpath: The path of the directory to generate the beacon in
    :param children_paths: The paths of the files to save in the beacon
    :param filename: The name of the beacon (optional)
    :return: The path of the generated beacon
    """

    #   1. Formatting the directory path (adding the final '/')
    dirpath = BFunc.format_dir_path(dirpath)

    #   2. Generating the beacon file's path
    beaconpath = f'{dirpath}{filename}'

    #   3. Opening the beacon file for writing
    with open(beaconpath, 'w', encoding='utf-8') as beacon:

        for childpath in children_paths:

            #   3.1. Calculating the size of the child file or directory
            size = IFunc.size_bytes(childpath)

            #   3.2. Generating the line
            line = f'{childpath}{_dsep_}{size}{_lsep_}'

            #   3.3. Writing to the file
            beacon.write(line)

    return beaconpath
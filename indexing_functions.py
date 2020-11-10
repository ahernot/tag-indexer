# FROM https://superuser.com/questions/22460/how-do-i-get-the-size-of-a-linux-or-mac-os-x-directory-from-the-command-line
import os
import subprocess

import preferences as Pref
import basic_functions as BFunc
import file_analysis as FFunc
import beacons_sizes, beacons_tags


_files_ = Pref._files_



def get_dir_contents(parent_dirpath: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(parent_dirpath):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list



def process_dir_dict_beacons(dir_path: str, skip_unmodified_dirs: bool = False, skip_unmodified_tags: bool = True):
    """
    Recursive function to process a directory
    :param dir_path: The path of the directory to analyse
    :param skip_unmodified_dirs: Skip directories whose total size in bytes hasn't changed since the last run of the program
    :return: The directory's hierarchy dictionary
    """

    def recur(parent_dirpath: str):

        #   1. Formatting the parent directory's path (making sure that a path separator is present at the end)
        parent_dirpath = BFunc.format_dir_path(parent_dirpath)

        #   2.1. Getting the contents of the parent directory
        dirnames_list, filenames_list = get_dir_contents(parent_dirpath)
        #   2.2. Adding the parent directory's path to get lists of paths
        dirpaths_list = [parent_dirpath + dirname for dirname in dirnames_list]
        filepaths_list = [parent_dirpath + filename for filename in filenames_list]



        #   3.1. Reading the parent directory's sizes beacon file
        if skip_unmodified_dirs:
            beacon_sizes_dict = beacons_sizes.read_beacon(parent_dirpath)
        #   3.2. Reading the parent directory's tags beacon file
        if skip_unmodified_tags:
            beacon_tags_dict = beacons_tags.read_beacon(parent_dirpath)



        #   4. Processing the child directories
        for dirname in dirnames_list:

            #   4.1. Getting the child directory's path
            dirpath = parent_dirpath + dirname

            #   4.2. Optional skipping of seemingly unmodified directories
            if skip_unmodified_dirs:

                #   4.2.1. Calculating the size of the child directory
                dirsize_bytes = size_bytes(dirpath)

                #   4.2.2. Skipping the processing of the branch if the beacon's value match the current ones
                if beacons_sizes.matches_beacon(beacon_sizes_dict, dirpath, dirsize_bytes):
                    continue

            #   4.3. Recursive call of the function to get the child directory's contents dictionary
            recur(dirpath)



        #   5. Processing the files
        for filepath in filepaths_list:

            #   5.1. Optional skipping of seemingly unmodified files
            if skip_unmodified_dirs:

                #   5.1.1. Calculating the size of the child directory
                filesize_bytes = size_bytes(filepath)

                #   5.1.2. Skipping the processing of the branch if the beacon's value match the current ones
                if beacons_sizes.matches_beacon(beacon_sizes_dict, filepath, filesize_bytes):
                    continue

            #   5.2. Reading the file's tags
            tags_list = FFunc.get_tags(filepath)

            #   5.3. Optional skipping of unmodified tags
            if skip_unmodified_tags:

                #   5.3.1. Skipping the processing of the file if the beacon's value match the current ones
                if beacons_tags.matches_beacon(beacon_tags_dict, filepath, tags_list):
                    continue




            print('GENERATING ALIASES')
            #use tags_analysis.py




        #   6.1. Regenerating the parent directory's sizes beacon file
        if skip_unmodified_dirs:
            beacons_sizes.write_beacon(parent_dirpath, dirpaths_list)
        #   6.2. Regenerating the parent directory's tags beacon file
        if skip_unmodified_tags:
            beacons_tags.write_beacon(parent_dirpath, filepaths_list)



    recur(dir_path)






## LEGACY FUNCTION
def get_dir_dict(dir_path: str) -> dict:
    """
    Recursive function to get all the contents of a directory.
    :param dir_path: The path of the directory to analyse
    :return: The directory's hierarchy dictionary
    """

    def recur(parent_dirpath: str) -> dict:

        #   1. Initialising the directory's dictionary
        dir_dict = dict()

        #   2. Formatting the parent directory's path (making sure that a path separator is present at the end)
        parent_dirpath = BFunc.format_dir_path(parent_dirpath)

        #   3. Getting the contents of the parent directory
        dirnames_list, filenames_list = get_dir_contents(parent_dirpath)

        #   4. Processing the child directories
        for dirname in dirnames_list:

            #   4.1. Getting the child directory's path
            dirpath = parent_dirpath + dirname

            #   4.2. Recursive call of the function to get the child directory's contents dictionary
            dir_dict[dirname] = recur(dirpath)

        #   5. Adding the files contained in the parent directory
        dir_dict[_files_] = [parent_dirpath + filename for filename in filenames_list if filename[0] != '.']

        return dir_dict

    main_dir_dict = recur(dir_path)

    return main_dir_dict





def size_bytes(path: str) -> int:
    cmd = ['find',
           path,
           '-type f -exec ls -l {} \; | awk \'{sum += $5} END {print sum}\''
           ]
    output_bytes = subprocess.check_output([' '.join(cmd)], shell=True)
    return int( output_bytes.decode('utf-8')[:-1] )

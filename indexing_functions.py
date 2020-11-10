# FROM https://superuser.com/questions/22460/how-do-i-get-the-size-of-a-linux-or-mac-os-x-directory-from-the-command-line
import os
import subprocess

import preferences as Pref
import basic_functions as BFunc
import beacons_sizes


_files_ = Pref._files_



def get_dir_contents(parent_dirpath: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(parent_dirpath):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list



def process_dir_dict_beacons(dir_path: str, skip_unmodified_dirs: bool = False):
    """
    Recursive function to process a directory
    :param dir_path: The path of the directory to analyse
    :param skip_unmodified_dirs: Skip directories whose total size in bytes hasn't changed since the last run of the program
    :return: The directory's hierarchy dictionary
    """

    def recur(parent_dirpath: str):

        #   1. Formatting the parent directory's path (making sure that a path separator is present at the end)
        parent_dirpath = BFunc.format_dir_path(parent_dirpath)

        #   2. Getting the contents of the parent directory
        dirnames_list, filenames_list = get_dir_contents(parent_dirpath)



        #   3. Reading the parent directory's beacon file
        beacon_dict = beacons_sizes.read_beacon(parent_dirpath)



        #   4. Processing the child directories
        for dirname in dirnames_list:

            #   4.1. Getting the child directory's path
            dirpath = parent_dirpath + dirname

            #   4.2. Calculating the size of the child directory
            dirsize_bytes = size_bytes(dirpath)

            #   4.3. Skipping the processing of the branch if the beacon's value match the current ones
            if beacons_sizes.matches_beacon(beacon_dict, dirpath, dirsize_bytes): continue

            #   4.4. Recursive call of the function to get the child directory's contents dictionary
            recur(dirpath)


        #   5. Processing the files


    recur(dir_path)

    #return main_dir_dict






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

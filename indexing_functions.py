import os

import basic_functions as BFunc



def get_dir_contents(parent_dirpath: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(parent_dirpath):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list



def get_dir_dict(dir_path: str) -> dict:
    """
    Recursive function to get all the contents of a directory.
    :param dir_path: The path of the directory to analyse
    :return: The directory's hierarchy dictionary
    """

    _files_ = '_files_'

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



dir_stat = os.stat('/Users/Anatole/Documents/TEST-directory-branching')
file_stat = os.stat('/Users/Anatole/Documents/TEST-directory-branching/file1.txt')
print(dir_stat)
print(file_stat)


import subprocess

def size_bytes(path: str) -> int:
    cmd = ['find',
           path,
           '-type f -exec ls -l {} \; | awk \'{sum += $5} END {print sum}\''
           ]
    return int( subprocess.check_output([' '.join(cmd)], shell=True).decode('utf-8')[:-1] )

# FROM https://superuser.com/questions/22460/how-do-i-get-the-size-of-a-linux-or-mac-os-x-directory-from-the-command-line
print(
    size_bytes(path = '/Users/Anatole/Documents/TEST-directory-branching')
)


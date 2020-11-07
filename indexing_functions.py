import os

import basic_functions as BFunc



def get_dir_contents(dir_path: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list



def get_all_files_stack(dir_path: str, lvl: int, run_id: int, main_dirs_list: list, main_filepaths_list: list):
    _psep_ = '/'

    #   1. Correcting directory_path to always end with '/'
    dir_path = BFunc.format_dir_path(dir_path)

    #   2.1. Incrementing the 'depth' level (the 'indentation')
    lvl += 1
    #   2.2. Incrementing run_id (for each separate run of the function, stacked since it is returned out of the function)
    run_id += 1

    #   3. Reading the current folder's sub-folders and single files
    dirnames_list, filenames_list = get_dir_contents(dir_path)

    #   4. Adding the current folder's data to the global data lists (in position run_id)
    main_dirs_list.append(dirnames_list)  # on position run_id

    #   5. Appending the path of each file in the current folder to the main filepaths list
    for filename in filenames_list:
        filepath = dir_path + filename
        main_filepaths_list.append(filepath)

    #   6. Running through the sub-folders
    for folder in main_dirs_list[run_id]:

        #   6.1. Generating the sub-folder's path
        sub_path = dir_path + folder + _psep_

        #   6.2. Running the current function for the sub-folder: will update run_id, main_folder_list (with one more item), and main_filepath_list (with all the new files) lists
        run_id, main_dirs_list , main_filepaths_list = get_all_files_stack(sub_path, lvl, run_id, main_dirs_list , main_filepaths_list)

    return run_id, main_dirs_list , main_filepaths_list


def get_all_files(dir_path: str):
    return get_all_files_stack(dir_path, 0, -1, [], [])[2]



x = get_all_files('/Users/Anatole/Documents')
print(x)


"""
REQ: dictionary with

dir
    subdir
        subsubdir
        file
    subdir
        subsubdir
        file
    file
    file

"""
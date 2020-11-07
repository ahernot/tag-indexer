import os

import basic_functions as BFunc



def get_dir_contents(dir_path: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list



def get_all_files_stack(dir_path: str, lvl, run_id, main_folder_list, main_filepath_list):
    #   1. Correcting directory_path to always end with '/'
    dir_path = BFunc.format_dir_path(dir_path)

    #   2. Incrementing the 'depth' level (the 'indentation')
    lvl += 1
    #   3. Incrementing run_id (for each separate run of the function, stacked since it is returned out of the function)
    run_id += 1


    #   4. Reading the current folder's sub-folders and single files
    dirnames_list, filenames_list = get_dir_contents(dir_path)


    #   5. Adding the current folder's data to the global data lists (in position run_id)
    main_folder_list.append(folders_list_temp)  # on position run_id



    #   6. Appending the path of each file in the current folder to the main filepaths list
    for file in files_list_temp:
        filepath = directory_path + file
        main_filepath_list.append(filepath)

    #   7. Running through the sub-folders
    for folder in main_folder_list[run_id]:
        #   7.1. Generating the sub-folder's path
        sub_path = directory_path + folder + '/'
        #   7.2. Running the current function for the sub-folder: will update run_id, main_folder_list (with one more item), and main_filepath_list (with all the new files) lists
        main_filepath_list, run_id, main_folder_list = get_all_files_stack(sub_path, lvl, run_id, main_folder_list,
                                                                           main_filepath_list)

    return main_filepath_list, run_id, main_folder_list


def get_all_files(directory_path):
    return get_all_files_stack(directory_path, 0, -1, [], [])[0]
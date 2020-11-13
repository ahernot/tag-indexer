"""
This file manages running through the file hierarchy and analysing accordingly.
FROM https://superuser.com/questions/22460/how-do-i-get-the-size-of-a-linux-or-mac-os-x-directory-from-the-command-line
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import os

#   IMPORTING PROJECT FILES
import preferences as Pref
import basic_functions as BFunc
import file_analysis as FFunc
import beacons_sizes as SBeacons
import beacons_tags as TBeacons
import tags_processing as Tags

#   DEFINING FILE-WIDE VARIABLES
_files_ = Pref._files_




def get_dir_contents(parent_dirpath: str):
    dirnames_list, filenames_list = list(), list()

    for (dirpath, dirnames, filenames) in os.walk(parent_dirpath):
        dirnames_list.extend(dirnames)
        filenames_list.extend(filenames)
        break

    return dirnames_list, filenames_list




def process_dir_beacons(dirpath: str, skip_unmodified_dirs: bool = False, regenerate_aliases: bool = False, display_progression: int = 100):
    """
    Recursive function to process a directory
    :param dir_path: The path of the directory to analyse
    :param skip_unmodified_dirs: Skip directories whose total size in bytes hasn't changed since the last run of the program
    :param regenerate_aliases: Regenerate aliases regardless of their existence (regenerate user-deleted alias files)
    :param display_progression: The rough number of progression steps to display.
    :return: The directory's hierarchy dictionary
    """

    #   0. Getting the number of files to process
    if display_progression:
        import math
        total_filecount = len(get_files_list(dirpath))
        display_every = math.ceil(total_filecount / display_progression)
        print(f'{total_filecount} files to process\n')


    def recur(parent_dirpath: str, filecount: int = 0):

        #   1. Formatting the parent directory's path (making sure that a path separator is present at the end)
        parent_dirpath = BFunc.format_dir_path(parent_dirpath)

        #   2.1. Getting the contents of the parent directory
        dirnames_list, filenames_list = get_dir_contents(parent_dirpath)
        #   2.2. Adding the parent directory's path to get lists of paths (and skipping hidden files)
        dirpaths_list = [parent_dirpath + dirname for dirname in dirnames_list]
        filepaths_list = [parent_dirpath + filename for filename in filenames_list if not(BFunc.ishidden(filename))]



        #   3.1. Reading the parent directory's sizes beacon file
        if skip_unmodified_dirs:
            beacon_sizes_dict = SBeacons.read_beacon(parent_dirpath)

        #   3.2. Reading the parent directory's tags beacon file
        beacon_tags_dict = TBeacons.read_beacon(parent_dirpath)



        #   4. Processing the child directories
        for dirname in dirnames_list:

            #   4.1. Getting the child directory's path
            dirpath = parent_dirpath + dirname


            #   4.2. Optional skipping of seemingly unmodified directories
            if skip_unmodified_dirs:

                #   4.2.1. Calculating the size of the child directory
                dirsize_bytes = BFunc.size_bytes(dirpath)

                #   4.2.2. Skipping the processing of the branch if the beacon's value match the current ones
                if SBeacons.matches_beacon(beacon_sizes_dict, dirpath, dirsize_bytes):
                    continue

            #   4.3. Recursive call of the function to get the child directory's contents dictionary
            filecount = recur(dirpath, filecount)



        #   5. Processing the files
        for filepath in filepaths_list:

            filecount += 1
            #   5.0. Displaying progression (optional)
            if display_progression:
                BFunc.display_progression(filecount, total_filecount, display_every)


            #   5.1. Optional skipping of seemingly unmodified files
            if skip_unmodified_dirs:

                #   5.1.1. Calculating the size of the child directory
                filesize_bytes = BFunc.size_bytes(filepath)

                #   5.1.2. Skipping the processing of the branch if the beacon's value match the current ones
                if SBeacons.matches_beacon(beacon_sizes_dict, filepath, filesize_bytes):
                    continue


            #   5.2. Reading the file's tags
            tags_list = FFunc.get_tags(filepath)

            #   5.3. Reading the beacon's stored tags for the file
            beacon_tags_list = list()
            try:
                beacon_tags_list = beacon_tags_dict[filepath]
            except KeyError:
                pass


            #   5.4.1. Calculating the difference with the values stored in the beacon
            tags_removed_list, tags_added_list = BFunc.diff_list(beacon_tags_list, tags_list)
            #   5.4.2. Adding all tags in the list of tags to generate aliases for
            if regenerate_aliases:
                tags_added_list = tags_list.copy()


            #   5.5. Skipping the iteration if no tags modified
            if (not tags_added_list) and (not tags_removed_list):
                continue


            #   5.6. Processing the tags to make and delete alias files
            unprocessed_tags_list = list()
            #   5.6.1. Making the aliases corresponding to the added tags
            unprocessed_tags_list += Tags.make_aliases(filepath, *tags_added_list)

            #   5.6.2. Deleting the aliases corresponding to the removed tags
            unprocessed_tags_list += Tags.remove_aliases(filepath, *tags_removed_list)



        #   6. Removing the aliases for deleted files
        removed_dict = TBeacons.get_removed_files(filepaths_list, beacon_tags_dict)
        for filepath in removed_dict:
            Tags.remove_aliases(filepath, *removed_dict[filepath])


        #   7.1. Regenerating the parent directory's sizes beacon file
        if skip_unmodified_dirs:
            SBeacons.write_beacon(parent_dirpath, dirpaths_list)

        #   7.2. Regenerating the parent directory's tags beacon file
        TBeacons.write_beacon(parent_dirpath, filepaths_list)


        return filecount



    #   Initial call of the recursive function
    recur(dirpath)




def get_dir_dict(dirpath: str) -> dict:
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

    #   Initial call of the recursive function
    main_dir_dict = recur(dirpath)

    return main_dir_dict




def get_files_list(dirpath: str) -> list:
    """
    This function generates a flat list (one-dimensional array) of all the non-hidden files contained in a directory and its subdirectories.
    :param dirpath: The directory's path
    :return: The list of files contained in the directory
    """

    import itertools

    filelist_deep = [files for _, _, files in os.walk(r'/Users/Anatole/Documents/TEST-directory-branching')]
    filelist_flat = itertools.chain.from_iterable(filelist_deep)
    filelist_flat_filtered = [file for file in filelist_flat if (not BFunc.ishidden(file))]

    return filelist_flat_filtered
#!/usr/bin/env python3

import os

from preferences import *


def remove_beacons (dirpath: str, beacon_name: str = BEACON_NAME):
    """
    Recursively remove all beacons from a directory and its subdirectories
    :param dirpath: path of the directory to alter
    :param beacon_name: filename of the beacon
    :return: None
    """
    
    def recur (dirpath: str, beacon_pathlist: list):

        # Initialise list of subdirs to parse
        subdirs = list()

        # Parse current dir
        with os.scandir (dirpath) as file_dir:

            for file in file_dir:

                if file.is_dir():
                    subdirs.append (file.path)
                
                else:
                    if file.name == beacon_name:
                        os.remove (file.path)


        # Recursively run for subdirs
        for subdirpath in subdirs:
            file_dict = recur (subdirpath, beacon_pathlist)
        
        return beacon_pathlist

    beacon_pathlist = recur (dirpath, list())

def clean_dir (dirpath: str):
    """
    Remove empty children folders within dirpath
    :param dirpath: path of the directory to alter
    :return: None
    """
    pass

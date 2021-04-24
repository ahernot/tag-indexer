#!/usr/bin/env python3

import os

from preferences import *


def read_dir (dirpath: str):

    def recur (dirpath: str, file_dict: dict):

        # Initialise list of subdirs to parse
        subdirs = list()

        # Generate beacon path (regardless of its existence)
        beacon_path = os.path.join (dirpath, BEACON_NAME)

        # Initialise dict entry
        file_dict [beacon_path] = list()

        # Parse current dir
        with os.scandir (dirpath) as file_dir:

            for file in file_dir:

                if file.is_dir():
                    subdirs.append (file.path)
                
                else:
                    file_dict [beacon_path] .append (file)  # OR append filepath

        # Recursively run for subdirs
        for subdirpath in subdirs:
            file_dict = recur (subdirpath, file_dict)
        
        return file_dict
    
    return recur( dirpath, dict() )

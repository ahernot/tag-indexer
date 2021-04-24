#!/usr/bin/env python3

import json
import os

from file_analysis import read_tags


def diff_lists (list_1: list, list_2: list):
    # case-sensitive, crude implementation, works very well for small lists

    add = list()
    remove = list()
    
    for item in list_1:
        if item not in list_2:
            remove.append (item)

    for item in list_2:
        if item not in list_1:
            add.append (item)

    return add, remove


def index_files (file_dict: dict, ignore_beacons = False):

    tag_add_dict = dict()
    tag_remove_dict = dict()
    
    # Run through beacons (subdirs)
    for beacon_path in file_dict:
        
        # Read JSON beacon
        if not os.path.exists (beacon_path) or ignore_beacons:
            beacon_dict = dict()
    
        else:
            with open (beacon_path, 'r', encoding='utf-8') as beacon:
                beacon_dict = json.load (beacon)
        
        # Run through files
        for file in file_dict [beacon_path]:
            
            # Read tags saved in beacon
            try: 
                saved_tags = beacon_dict [file.name]
            except KeyError:
                saved_tags = list()
            
            # Read current tags
            current_tags = read_tags (file.path)  # returns empty list for missing file

            # Compute differences
            add, remove = diff_lists (saved_tags, current_tags)

            # Queue for processing
            for tag in add:
                try:
                    tag_add_dict [tag] .append (file.path)
                except KeyError:
                    tag_add_dict [tag] = [file.path]

            for tag in remove:
                try:
                    tag_remove_dict [tag] .append (file.path)
                except KeyError:
                    tag_remove_dict [tag] = [file.path]
            
            # Update beacon dict
            beacon_dict [file.name] = current_tags

        # Write beacon                
        with open (beacon_path, 'w', encoding='utf-8') as beacon:
            json.dump (beacon_dict, beacon, indent=4)

    return tag_add_dict, tag_remove_dict

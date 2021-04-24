#!/usr/bin/env python3

import json
import os

# from preferences import *


def index_files (file_dict: dict):

    for beacon_path in file_dict:
        
        if not os.path.exists (beacon_path):
            beacon_dict = dict()
    
        else:
            # data_dict = {'IMG_2020.JPG': ['tag1'], 'IMG_1934.JPG': ['tag1', 'tag2']}
            # with open (beacon_path, 'w', encoding='utf-8') as beacon:
            #     beacon_dict = json.dump (data_dict, beacon, indent=4)
            with open (beacon_path, 'r', encoding='utf-8') as beacon:
                beacon_dict = json.load (beacon)
        


        for filepath in file_dict [beacon_path]:  #TODO: or else file OBJECT
            
            # read tags
            # match tags with those on beacon, if any
            # mark added tags for +ALIAS (hard-stored > on startup, rundown this task list first)
            # mark removed tags for -ALIAS (hard-stored)
            # update beacon
#!/usr/bin/env python3

import json

# from preferences import *


def index_files (file_dict: dict):

    for beacon_path in file_dict:
        
        if not path.exists (beacon_path):
            beacon_dict = dict()
    
        else:
            with open (beacon_path, 'r', encoding='utf-8') as beacon:
                beacon_dict = json.load (beacon)
        
        print(beacon_dict)

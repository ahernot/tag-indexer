#!/usr/bin/env python3

import os

from alias_builder import make_alias


"""
goals for this file:
* generate alias folder (processed tag name)
* generate alias name (datetime, …)
* make alias file
* destroy alias file
"""


def process_tag (tag: str):
    # to do
    return tag


def add_aliases (tag_add_dict: dict):

    for tag in tag_add_dict:

        # Format tag name
        tag_name = process_tag (tag)

        # Create alias directory
        alias_dirpath = ''

        try:
            os.makedirs (alias_dirpath)
        except FileExistsError:
            pass

        # Run through files
        for file in tag_name:
            
            # Generate alias filename
            alias_name = file.name
            
            # Make alias
            make_alias (file.path, alias_dirpath, alias_name)






    pass


def remove_aliases (tag_remove_dict: dict):
    pass

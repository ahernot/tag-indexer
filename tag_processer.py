#!/usr/bin/env python3

import os

from alias_builder import make_alias
from preferences import *


"""
goals for this file:
* generate alias folder (processed tag name)
* generate alias name (datetime, …)
* make alias file
* destroy alias file

to do:
add update big aliases database >> can build file hyperlinks too
"""


def process_tag_arg (tag_arg: str, instr: str or None = None) -> str:
    """
    Process tag argument
    """

    # No instruction
    if instr is None:
        return tag_arg

    # Instruction space-before-uppercase
    if instr == 'space-before-uppercase':
        tag_arg_new = tag_arg [0]

        # Add space before uppercase
        for char in tag_arg [1:]:
            if char.isupper():
                tag_arg_new += f' {char}'
            else:
                tag_arg_new += char

        return tag_arg_new



# case-sensitive
def process_tag (tag: str):
    """
    Generate tag dirpath

    """

    # Run through referenced tags
    for otag in TAGS_DICT:

        # If exact match (specific tag)
        if tag == otag:

            # Extract tag directory and subdirectory
            tag_dir, tag_subdir = TAGS_DICT [otag]

            # Generate tag dirpath
            tag_dirpath = os.path.join (tag_dir, tag_subdir)
            return tag_dirpath

        # Check match with placeholder tag
        elif otag [-1] == RTAG:
            
            # Extract root of placeholder tag
            otag_root = otag [:-1]
            otag_rootlen = len (otag_root)

            # If match with placeholder tag
            if tag [:otag_rootlen] == otag_root:

                # Extract argument (to replace RTAG placeholder with)
                tag_arg = tag [otag_rootlen:]

                # Extract tag directory and subdirectory
                tag_dir, tag_subdir, instr = TAGS_DICT [otag]

                # Process tag_arg (for example, add spaces before capital letters)
                tag_arg = process_tag_arg (tag_arg, instr)

                # Replace occurrences of RTAG placeholder in subdir
                while RTAG in tag_subdir:
                    tag_subdir = tag_subdir.replace (RTAG, tag_arg)

                # Generate tag dirpath
                tag_dirpath = os.path.join (tag_dir, tag_subdir)
                return tag_dirpath

    # Run only if no match
    tag_dirpath = os.path.join (TAG_NOCAT, tag)
    return tag_dirpath





def add_aliases (tag_add_dict: dict):

    for tag in tag_add_dict:

        # Generate tag dirpath
        tag_dirpath = process_tag (tag)

        try:
            os.makedirs (alias_dirpath)
        except FileExistsError:
            pass

        # Run through files
        for file in tag_name:
            
            # Generate alias filename
            alias_name = file.name
            ### TO COMPLETE
            
            # Make alias
            make_alias (file.path, alias_dirpath, alias_name)






    pass


def remove_aliases (tag_remove_dict: dict):
    pass


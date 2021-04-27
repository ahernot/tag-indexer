#!/usr/bin/env python3

import os
import posix

from aliaser import make_alias
from file_analysis import get_birthtime_formatted
from preferences import *
from logger import Log


"""
goals for this file:
* generate alias name (datetime, …)

to do:
add update big aliases database >> can build file hyperlinks too
"""


def process_tag_arg (tag_arg: str, instr: str or None = None) -> str:
    """
    Process tag argument
    :param tag_arg: tag argument
    :param instr: processing instruction
    :return: processed tag argument
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

def generate_tag_dirpath (tag: str):
    """
    Generate tag dirpath using the rules specified in preferences.py
    Case-sensitive
    :param tag: tag to generate for
    :return: dirpath
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

def generate_alias_relpath (file: posix.DirEntry):
    """
    Generate alias subdirectory and filename
    :param file: file to alias
    :return: alias subdirectory's relative path, alias filename
    """

    alias_dirpath_rel = ''
    alias_name = f'{get_birthtime_formatted (file)} – {file.name}'

    return alias_dirpath_rel, alias_name

def add_aliases (output_dirpath: str, tag_add_dict: dict, log: Log = None):
    """
    Create file aliases
    :param output_dirpath: alias files' parent dirpath
    :param tag_add_dict: tags to add for
    :param log: log
    :return: none
    """

    # Run through tags
    for tag in tag_add_dict:

        # Generate tag dirpath
        tag_dirpath_rel = generate_tag_dirpath (tag)
        tag_dirpath = os.path.join (output_dirpath, tag_dirpath_rel)

        try:
            os.makedirs (tag_dirpath)
        except FileExistsError:
            pass

        # Run through files
        for file in tag_add_dict [tag]:
            
            # Generate alias filename
            alias_dirpath_rel, alias_name = generate_alias_relpath (file)
            alias_dirpath = os.path.join (tag_dirpath, alias_dirpath_rel)

            try:
                os.makedirs (alias_dirpath)
            except FileExistsError:
                pass
            
            # Make alias
            alias_path = make_alias (file.path, alias_dirpath, alias_name)

            ### TODO: MODIFY ALIAS CREATION DATE

def remove_aliases (output_dirpath: str, tag_remove_dict: dict, log: Log = None):
    """
    Delete file aliases
    :param output_dirpath: alias files' parent dirpath
    :param tag_add_dict: tags to add for
    :param log: log
    :return: none
    """

    for tag in tag_remove_dict:

        # Generate tag dirpath
        tag_dirpath_rel = generate_tag_dirpath (tag)
        tag_dirpath = os.path.join (output_dirpath, tag_dirpath_rel)

        # Run through files
        for file in tag_remove_dict [tag]:
            
            # Generate alias path
            alias_dirpath_rel, alias_name = generate_alias_relpath (file)
            alias_path = os.path.join (tag_dirpath, alias_dirpath_rel, alias_name)
            
            # Remove alias
            try:
                os.remove (alias_path)
            except FileNotFoundError:
                log.add_line (f'{LOGMSG_MISSING_DELETE} {alias_path}')  # write to log

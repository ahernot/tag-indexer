#!/usr/bin/env python3

from parser import read_dir
from indexer import index_files
from tag_processer import add_aliases, remove_aliases

from functions import dictlen


def process_dir (dirpath: str, output_dirpath: str, ignore_beacons = False):

    # Parse directory
    file_dict = read_dir (dirpath)

    # Index files according to tags
    tag_add_dict, tag_remove_dict = index_files (file_dict, ignore_beacons=ignore_beacons)

    print (f'Adding {dictlen(tag_add_dict)} aliases.\nRemoving {dictlen(tag_remove_dict)} aliases.')

    # Make aliases
    add_aliases (output_dirpath, tag_add_dict)

    # Destroy aliases




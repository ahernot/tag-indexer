#!/usr/bin/env python3

from parser import read_dir
from indexer import index_files


def process_dir (dirpath: str, output_dirpath: str, ignore_beacons = False):

    # Parse directory
    file_dict = read_dir (dirpath)

    # Index files according to tags
    tag_add_dict, tag_remove_dict = index_files (file_dict, ignore_beacons=ignore_beacons)

    print(tag_add_dict, tag_remove_dict)

    # Make aliases

    # Destroy aliases




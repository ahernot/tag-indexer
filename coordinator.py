#!/usr/bin/env python3

from parser import read_dir
from indexer import index_files
from tag_processer import add_aliases, remove_aliases
from cleaner import clean_dir

from logger import Log

from functions import dictlen


def process_dir (dirpath: str, output_dirpath: str, ignore_beacons: bool = False):
    """
    Generate aliases for the children of a dirpath
    :param dirpath: dirpath to process
    :param output_dirpath: output dirpath
    :param ignore_beacons: ignore beacons marking already generated aliases
    :return: None
    """

    # Instantiate log
    log = Log (dirpath=output_dirpath)

    # Parse directory
    file_dict = read_dir (dirpath)

    # Index files according to tags
    tag_add_dict, tag_remove_dict = index_files (file_dict, ignore_beacons=ignore_beacons)

    log.add_line (f'Adding {dictlen(tag_add_dict)} aliases.')
    log.add_line (f'Removing {dictlen(tag_remove_dict)} aliases.')

    # Add aliases
    add_aliases (output_dirpath, tag_add_dict, log)

    # Remove aliases
    remove_aliases (output_dirpath, tag_remove_dict, log)

    # Clean aliases' directory
    clean_dir (output_dirpath)

    # Save log
    log.save()

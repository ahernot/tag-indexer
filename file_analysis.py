#!/usr/bin/env python3

import xattr
import json
from subprocess import Popen, PIPE
import os
import datetime
import posix

from preferences import *


def bplist_to_list (bplist: bytes) -> list:
    """
    Decode bplist bytestrings
    Adapted from https://stackoverflow.com/questions/8856032/reading-binary-plist-files-with-python
    :param bplist: bplist to decode
    :return: the bplist's list representation
    """

    args = ['plutil', '-convert', 'json', '-o', '-', '--', '-']
    p = Popen(args, stdin=PIPE, stdout=PIPE)
    out, err = p.communicate(bplist)

    return json.loads (out)

def read_tags (filepath: str) -> list:
    """
    Read the tags of a file/directory (macOS-specific)
    :param filepath: filepath to analyse
    :return: list of tags
    """

    try:
        tagattr = xattr.getxattr (filepath, 'com.apple.metadata:_kMDItemUserTags')

        tags = bplist_to_list (tagattr)

        tags = [tag.split('\n')[0] for tag in tags]
        return tags

    except:
        return list()

# TODO: this function must implement a priority system for sources:
# 1. EXIF
# 2. File birthtime
def get_birthtime_formatted (file: posix.DirEntry) -> str:
    """
    Get the birthtime of a file as a formatted string
    :param filepath: filepath to analyse
    :return: formatted datetime string
    """
    birthtime = os.stat (file.path) .st_birthtime
    birthtime_formatted = datetime.datetime.fromtimestamp (birthtime) .strftime (ALIAS_DATETIME_FORMAT)
    return birthtime_formatted

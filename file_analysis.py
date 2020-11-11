"""
This file manages reading tags from files.
"""

#   IMPORTING THIRD-PARTY LIBRARIES
import xattr
import json
from subprocess import Popen, PIPE

#   IMPORTING PROJECT FILES
import preferences as Pref

#   DEFINING FILE-WIDE VARIABLES
_lsep_ = Pref._lsep_



def bplist_to_list(bplist: bytes) -> list:
    """
    This function decodes bplist bytes strings. Adapted from https://stackoverflow.com/questions/8856032/reading-binary-plist-files-with-python.
    :param bplist: The bplist to decode
    :return: The bplist's list representation
    """

    args = ['plutil', '-convert', 'json', '-o', '-', '--', '-']
    p = Popen(args, stdin=PIPE, stdout=PIPE)
    out, err = p.communicate(bplist)

    return json.loads(out)



def get_tags(filepath: str) -> list:
    """
    This function reads the tags of a file/directory (macOS-specific).
    :param filepath: The path of the file/directory to analyse
    :return: The list of tags
    """

    try:
        tagattr = xattr.getxattr(filepath, 'com.apple.metadata:_kMDItemUserTags')

        tags_list = bplist_to_list(tagattr)

        tags_list = [tag.split(_lsep_)[0] for tag in tags_list]
        return tags_list

    except:
        return list()
#!/usr/bin/env python3

import datetime


def dictlen (tag_dict: dict):
    """
    Get the total length of all the elements of a dict like {key: [elements_list]}
    :param tag_dict: dictionary to analyse
    :return: combined length of the dictionary's elements
    """
    l = 0

    for tag in tag_dict:
        l += len (tag_dict [tag])
    
    return l

def get_datetime (datetime_format: str):
    """
    Get the current datetime as a formatted string
    :param datetime_format: format string
    :return: formatted datetime string
    """
    
    return datetime.datetime.now () .strftime (datetime_format)

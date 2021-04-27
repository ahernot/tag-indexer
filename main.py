#!/usr/bin/env python3

"""
File indexing utility
@author: Anatole Hernot
@version: 2.0
"""

import sys

from coordinator import process_dir


if __name__ == '__main__':
    
    if len(sys.argv) == 3:

        process_dir (sys.argv[1], sys.argv[2], ignore_beacons=True)

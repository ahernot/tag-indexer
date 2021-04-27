#!/usr/bin/env python3

"""
File indexing utility
@author: Anatole Hernot
@version: 2.0.1
"""

import sys

from coordinator import process_dir


# Ignore beacons during alias creation
IGNORE_BEACONS = False

if __name__ == '__main__':
    
    if len(sys.argv) == 3:

        process_dir (sys.argv[1], sys.argv[2], ignore_beacons=IGNORE_BEACONS)

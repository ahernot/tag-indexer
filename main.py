#!/usr/bin/env python3

"""
File indexing utility
@author: Anatole Hernot
@version: 2.0
"""

import sys

# import indexing_functions as IFunc


# if __name__ == '__main__':
    
#     if len(sys.argv) == 2:  # 3:
#         IFunc.process_dir_beacons( sys.argv[1], regenerate_aliases=True )  #, sys.argv[2] )
#         # print( IFunc.get_files_list( sys.argv[1] ) )


## TESTS
# file_analysis.py (to rework)
# parser.py
# indexer.py

import parser
import indexer

TEST_PATH = '/Users/anatole/Downloads/_TEST_PYTAGS_'
file_dict = parser.read_dir (TEST_PATH)
i = indexer.index_files (file_dict)

#!/usr/bin/env python3

import sys

import indexing_functions as IFunc


if __name__ == '__main__':
    
    if len(sys.argv) == 2:  # 3:
        IFunc.process_dir_beacons( sys.argv[1] )  #, sys.argv[2] )
        # print( IFunc.get_files_list( sys.argv[1] ) )

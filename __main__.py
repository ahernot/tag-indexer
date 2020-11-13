#!/usr/bin/env python3

#   IMPORTING THIRD-PARTY LIBRARIES
# -

#   IMPORTING PROJECT FILES
import preferences as Pref
import indexing_functions as IFunc

#   DEFINING FILE-WIDE VARIABLES
main_directory = Pref.dir_to_process




if __name__ == '__main__':

    IFunc.process_dir_beacons(main_directory)

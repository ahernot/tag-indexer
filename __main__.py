#!/usr/bin/env python3

#   IMPORTING THIRD-PARTY LIBRARIES
# -

#   IMPORTING PROJECT FILES
import applescript as AS
import preferences as Pref
import indexing_functions as IFunc

#   DEFINING FILE-WIDE VARIABLES
main_directory = Pref.dir_to_process


def run():

    #   1. Analysing the main directory if ETA calculation (to know the number of files to process
    #THIS CODE WILL HAVE TO MOVE TO THE IFunc.process_dir_dict_beacons FUNCTION!!!
    if Pref.ETA_calculation:
        dir_dict = IFunc.get_dir_dict(main_directory)
        ### ADD A BOOL OPTION TO COUNT THE NUMBER OF FILES // GET STATS
        ### AND A BOOL OPTION TO GET A FLAT LIST OF FILES TOO

    IFunc.process_dir_beacons(main_directory)




if __name__ == '__main__':
    run()
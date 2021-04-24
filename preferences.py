
import os

#   DEFINING FILE-WIDE VARIABLES
main_path = os.path.realpath(__file__).replace('preferences.py', '')
preferences_path = main_path + 'preferences.txt'



# BEGIN UPDATED FILE
BEACON_NAME = '.pytags-beacon'






_files_ = '_files_'

_dbsep_ = '\t' # database separator
_dsep_ = '\t' # data separator
_lsep_ = '\n' # line separator
_psep_ = '/' # path separator
_esep_ = '.' # extension separator
_tsep_ = ', ' # tags list separator
_ssep_ = ' ' # space separator


alias_dir = 'TEST-generated-aliases/'

tag_placeholder	= '%'
database_name = 'database.txt'
beacon_tags_name = '.pytags_tags'
beacon_sizes_name = '.pytags_sizes'

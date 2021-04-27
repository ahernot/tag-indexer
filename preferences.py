
import os

#   DEFINING FILE-WIDE VARIABLES
main_path = os.path.realpath(__file__).replace('preferences.py', '')
preferences_path = main_path + 'preferences.txt'



# BEGIN UPDATED FILE
LOG_FILENAME = 'log.txt'
BEACON_NAME = '.pytags-beacon'

ALIAS_DATETIME_FORMAT = '%Y%m%d-%H%M%S'
LOG_DATETIME_FORMAT = '%Y%m%d-%H%M%S'

LOGMSG_MISSING_DELETE = 'Unable to find path for deletion:'

RTAG = '%'
TAG_NOCAT = 'Others'

# placeholder can only be the last element of the string, and only in subdir
# for tags with placeholder: [dir, subdir, format-instructions]
TAGS_DICT = {
    # Specific tags
    'Awesome Photo': ['Ratings', 'Awesome Photos'],
    'Awesome Picture': ['Ratings', 'Awesome Photos'],  # legacy
    'Awesome Video': ['Ratings', 'Awesome Videos'],
    'Great Photo': ['Ratings', 'Great Photos'],
    'Great Picture': ['Ratings', 'Great Photos'],  # legacy
    'Great Video': ['Ratings', 'Great Videos'],
    'Great Memories': ['Ratings', 'Great Memories'],
    'Funny Picture': ['Ratings', 'Funny Picture'],

    # Placeholder tags
    f'type {RTAG}': ['Types', RTAG, None],
    f'camera {RTAG}': ['Cameras', RTAG, None],
    f'people {RTAG}': ['People', RTAG, None],  # people in the photo/video
    f'subject {RTAG}': ['Subjects', RTAG, None],  # photo/video subject (not a person)
    f'shot by {RTAG}': ['Photographers', RTAG, None],

    # Legacy placeholder tags
    f'type{RTAG}': ['Types', RTAG, 'space-before-uppercase'],
    f'camera{RTAG}': ['Cameras', RTAG, 'space-before-uppercase'],
    f'people{RTAG}': ['People', RTAG, 'space-before-uppercase'],
    f'subject{RTAG}': ['Subjects', RTAG, 'space-before-uppercase'],
    f'scene{RTAG}': ['Scenes (legacy)', RTAG, 'space-before-uppercase'],
    f'shotby{RTAG}': ['Photographers', RTAG, 'space-before-uppercase']
}






_files_ = '_files_'

_dbsep_ = '\t' # database separator
_dsep_ = '\t' # data separator
_lsep_ = '\n' # line separator
_psep_ = '/' # path separator
_esep_ = '.' # extension separator
_tsep_ = ', ' # tags list separator
_ssep_ = ' ' # space separator


# alias_dir = 'TEST-generated-aliases/'

# tag_placeholder	= '%'
# database_name = 'database.txt'
# beacon_tags_name = '.pytags_tags'
# beacon_sizes_name = '.pytags_sizes'



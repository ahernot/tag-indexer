VERSION = '2.0.0'

# BEGIN UPDATED FILE
LOG_FILENAME = 'log.txt'
BEACON_NAME = '.pytags-beacon'

# Datetime formats
ALIAS_DATETIME_FORMAT = '%Y%m%d-%H%M%S'
LOG_DATETIME_FORMAT = '%Y%m%d-%H%M%S'

# Log messages
LOGMSG_MISSING_DELETE = 'Unable to find path for deletion:'
LOGREC_MISSING_DELETE = 'Recommend database deletion and reindexing'  # to implement
LOGMSG_DUPLICATE_ALIAS = 'Alias file already exists:'  # to implement
LOGREC_DUPLICATE_ALIAS = 'Recommend database deletion and reindexing'  # to implement

# Tags
RTAG = '%'
TAG_NOCAT = 'Others'

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

# placeholder can only be the last element of the string, and only in subdir
# for tags with placeholder: [dir, subdir, format-instructions]

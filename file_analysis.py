import xattr
import json
from subprocess import Popen, PIPE



def bplist_to_list(bplist: bytes) -> list:
    # from https://stackoverflow.com/questions/8856032/reading-binary-plist-files-with-python

    args = ['plutil', '-convert', 'json', '-o', '-', '--', '-']
    p = Popen(args, stdin=PIPE, stdout=PIPE)

    out, err = p.communicate(bplist)

    return json.loads(out)



def get_tags(filepath: str) -> list:
    try:
        tagattr = xattr.getxattr(filepath, 'com.apple.metadata:_kMDItemUserTags')
        return bplist_to_list(tagattr)
    except:
        return list()
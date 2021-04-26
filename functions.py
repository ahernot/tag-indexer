
def dictlen (tag_dict: dict):
    l = 0

    for tag in tag_dict:
        l += len (tag_dict [tag])
    
    return l

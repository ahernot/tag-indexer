
def dictlen (tag_dict: dict):
    l = 0

    for tag in tag_dict:
        l += len (tag_dict [tag])
    
    return l


# folder cleaner function to run at the end to find empty folders and delete them

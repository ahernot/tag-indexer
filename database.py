import basic_functions as BFunc
import preferences as Pref

_dsep_ = Pref._dsep_
_psep_ = Pref._psep_

default_parent_folder = 'Syntax/'
_stop_ = '__STOP__'
indent_marker = _dsep_
indent_len = len(indent_marker)
line_indent_parent = 0
line_indent_child  = 1


def read() -> dict:
    """
    This function reads the tags database provided by the user and generates a dictionary from it.
    :return: The tags dictionary
    """

    #   1.1. Initialising the tags dictionary
    tags_dictionary = dict()
    #   1.2. Initialising the parent folder
    parent_folder = default_parent_folder

    #   2. Reading the database file
    with open(Pref.database_path, 'r', encoding='utf-8') as tags_database:
        tags_database_list = tags_database.readlines()

    #   3. Processing the database's lines
    for line in tags_database_list + [_stop_]:

        #   3.0. Skipping the iteration if the parent folder is the default one
        if parent_folder == default_parent_folder: continue

        #   3.1. Counting the indentation level of the line
        line_indent = BFunc.count_indent(line, indent_marker)

        #   3.2. Removing all line breaks and indentation from the line
        line = BFunc.remove_chars(line, '\n')
        line_raw = line[line_indent * indent_len:]

        #   3.3. Skipping the iteration if the line is empty
        if not line_raw: continue

        #   3.4. Setting the new parent folder
        if line_indent == line_indent_parent:
            #   3.4.1. Making sure that a path separator is present at the end
            parent_folder = BFunc.format_dir_path(line_raw)

        #   3.5. (no tolerance for mismanaged indents)
        elif line_indent == line_indent_child:

            #   3.5.1. Splitting along the data separator
            line_split = line.split(_dsep_)
            if len(line_split) != 2: continue

            #   3.5.2. Unpacking
            tag_name, tag_folder = line_split

            #   3.5.3. Formatting the tag folder
            tag_path = parent_folder + tag_folder
            tag_path = BFunc.format_dir_path(tag_path)

            #   3.5.4. Adding the tag to the dictionary
            tags_dictionary[tag_name] = tag_path

    return tags_dictionary
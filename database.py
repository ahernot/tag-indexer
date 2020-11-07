import basic_functions as BFunc



indent_marker = '\t'
database_path = 'database.txt'
_stop_ = '__STOP__'

line_indent_parent = 0
line_indent_child = 1

with open(database_path, 'r', encoding='utf-8') as tags_database:
    tags_database_list = tags_database.readlines()


tags_dictionary = dict()
child_list = list()

indent_len = len(indent_marker)

parent_folder = ''
for line in tags_database_list + [_stop_]:

    #   .1. Counting the idndentation level of the line
    line_indent = BFunc.count_indent(line, indent_marker)

    #   .2. Removing all line breaks and indentation from the line
    line = BFunc.remove_chars(line, '\n')
    line_raw = line[line_indent * indent_len:]

    #   .3. Skipping iteration if the line is empty
    if not line_raw: continue

    #   .4.
    if line_indent == line_indent_parent:
        parent_folder = line_raw


    #   .5. No tolerance for mismanaged indents
    elif line_indent == line_indent_child:
        tag_name = '' # unique
        tag_path = ''
        #then build tag path
        #then add tag_name: tag_path to the dictionary

        tags_dictionary[tag_name] = tag_path
import preferences as Pref

def count_indent(line: str, indent_marker: str = '\t') -> int:
    """
    This function counts the indentation level of a given string.
    :param line: The line to count the indentation level for
    :param indent_marker: Indent marker (optional)
    :return: The indentation level of the line
    """
    indent_len = len(indent_marker)
    indent = 0
    while line and line[:indent_len] == indent_marker:
        indent += 1
        line = line[indent_len:]
    return indent




def replace_char(line:str, char: str, replacement: str = '') -> str:
    while char in line:
        line = line.replace(char, replacement)
    return line

def replace_chars(line: str, chars_dict: dict) -> str:
    for char_to_replace in chars_dict:
        line = replace_char(line, char_to_replace, chars_dict[char_to_replace])
    return line

def remove_chars(line: str, *chars: str) -> str:
    for char_to_remove in chars:
        line = replace_char(line, char_to_remove)
    return line

def remove_on_edges(line: str, *chars: str) -> str:
    for char_to_remove in chars:
        while line[0] == char_to_remove:
            line = line[1:]
        while line[-1] == char_to_remove:
            line = line[:-1]
    return line

def format_dir_path(dir_path: str):
    _psep_ = Pref._psep_
    if dir_path[-1] != _psep_:
        dir_path += _psep_
    return dir_path
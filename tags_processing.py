"""
This file manages interpreting the tags database.

TO ADD:
* case-insensitivity when processing tags
* alias name includes file DATE (either according to folders, metadata, file metadata, or custom hidden metadata file
* add a tag_placeholder value; replace all the [-1] and [:-1] with [-len], [:-len]
* in special_tags_match: ADD EXCEPTIONS WHEN SPLICING STRINGS AND OVERRUNNING THE TOTAL LENGTH (IndexError)
* WILL NEED AN OS.MAKEDIRS AT SOME POINT

CAREFUL: '%' MUST BE AT THE END OF THE TAG NAME (LAST CHARACTER)
"""

#   IMPORTING THIRD-PARTY LIBRARIES
# -

#   IMPORTING PROJECT FILES
import applescript
import database
import preferences as Pref
import basic_functions as BFunc

#   DEFINING FILE-WIDE VARIABLES
tags_dictionary = database.read()
tag_placeholder = Pref.tag_placeholder
_ssep_ = Pref._ssep_
special_tags_dict = dict([ (tag_name, tags_dictionary[tag_name]) for tag_name in tags_dictionary if tag_name[-1] == tag_placeholder ])





def format_tag_data(tag_data: str) -> str:
    """
    This function formats a tag data string by inserting spaces before capital letters.
    :param tag_data: The tag data strirng to format
    :return: The formatted tag data string
    """

    #   1. Initialising the formatted tag_data string
    tag_data_formatted = str()

    #   2. Running through the raw tag_data string's characters
    for char in tag_data:

        #   2.1. Adding a leading space separator if the character is uppercase
        if char.isupper():
            tag_data_formatted += _ssep_

        #   2.2. Adding the character, regardless of its type
        tag_data_formatted += char

    #   3. Cleaning up the formatted string (removing any leading and trailing space separators)
    tag_data_formatted = BFunc.remove_on_edges(tag_data_formatted, _ssep_)

    return tag_data_formatted





def generate_alias_name(filepath: str) -> str:
    """
    This function generates an alias name based on a predfined template for a specific filepath.
    :param filepath: The path of the file to alias
    :return: The name of the alias file
    """

    #   1. Generating the alias name's template
    alias_name = '{date}-{name}-alias'

    #   2. Processing the filepath
    dirpath, filename = BFunc.split_filepath(filepath)
    name, extension = BFunc.split_filename(filename)

    #   3. Getting the formatted creation date string (will look at file creation date only)
    date = BFunc.get_date_formatted(filepath)

    #   4. Generating the formatting dictionary
    format_dict = {
        'date': date,
        'name': name
    }

    #   5. Formatting the alias name
    alias_name.format(**format_dict)

    return alias_name




def remove_aliases(filepath: str, *tags: str):
    pass



def make_aliases(filepath: str, *tags: str) -> list:
    """
    This function creates alias files of files according to specific tags.
    :param filepath: The path of the original file
    :param tags: The tags to alias the file for
    :return: The list of unprocessed tags
    """

    #   0. Generating a list of unprocessed tags
    unprocessed_tags_list = list()

    #   1. Generating the name of the alias file
    alias_name = generate_alias_name(filepath)

    #   2. Processing the specified tags to alias the file for
    for tag in tags:
        is_processed = False

        #   2.1. Looking for exact matches with the user-specified tags
        if tag in tags_dictionary:

            #   2.1.1. Generating the alias' path
            tag_path = tags_dictionary[tag]
            alias_path = tag_path + alias_name

            #   2.1.2. Making the alias file and updating the flag
            applescript.make_alias(filepath, alias_path)
            is_processed = True

        #   2.2. Looking for format-specific matches with the user-specified special tags (if no exact matches found)
        else:

            tag_path = special_tags_match(tag)

            if tag_path:
                #   2.1.1. Generating the alias' path
                alias_path = tag_path + alias_name

                #   2.1.2. Making the alias file and updating the flag
                applescript.make_alias(filepath, alias_path)
                is_processed = True

        #   2.3. Logging unprocessed (unrecognised) tags
        if not is_processed:
            unprocessed_tags_list.append(tag)

    return unprocessed_tags_list





def special_tags_match(file_tag: str) -> str:
    """
    This function looks for matches with placeholder-containing user-defined tags.
    :param file_tag: The file tag to use for match pairing
    :return: The path of the (first) matching tag
    """

    #   1. Initialising the tag path variable (will be returned as is if no match found)
    tag_path = ''

    #   2. Running through the special (placeholder-containing) tags
    for special_tag in special_tags_dict:

        #   2.1. Extracting the tag base
        tag_base = special_tag[:-1]
        base_len = len(tag_base)

        #   2.2. Skipping the iteration if the tags do not match (add case-insensitivity here)
        if tag_base != file_tag[:base_len]:
            continue

        #   2.3. Extracting the tag data
        tag_data = file_tag[base_len:]

        #   2.4. Formatting the tag data
        tag_data_formatted = format_tag_data(tag_data)

        #   2.5. Generating the tag path
        tag_path = special_tags_dict[special_tag]
        tag_path = tag_path.replace(tag_placeholder, tag_data_formatted)

        break


    return tag_path
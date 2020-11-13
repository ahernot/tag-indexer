# tag-indexer v1.0.0
This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.


<br><br>
## To do
* v1.0.1: Add instructions of use
* v1.1: Add an actions log (useful?)
* v1.2: Add a `case_sensitivity` setting in `preferences.py`
* v2: Only save processed tags (not in `unprocessed_tags_list`) to the `.pytags_tags` beacon
* v2: Comply with sorting system hierarchies for reading actual file creation time and writing it to the alias file's name


<br><br>
## Changelog
* v0.9.0: Fully functional pre-release
* v0.9.1: Added alias regeneration, improved file processing (skipping hidden files)
* v1.0.0: Cleaned up `preferences.py`, added docstrings and file documentation, added a live progress tracker


<br><br>
## Working principle
* Retrieving tags to process from the tags database
* Running through the directories to decipher changes
* Change will be compared with the contents of the '.pytags_tags' hidden file
* Only files' tags will be accounted for by the program


<br><br>
## Instructions
* To be continued
* To display hidden files (macOS): type `defaults write com.apple.finder AppleShowAllFiles YES` in the macOS Terminal app
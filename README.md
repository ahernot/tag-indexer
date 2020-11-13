# tag-indexer v1.0.0

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.


<br><br>
## To do
* v1.1: Add an actions log (useful?)
* v2: Add a `case_sensitivity` setting in `preferences.py`
* v2: Only save processed tags (not in `unprocessed_tags_list`) to the `.pytags_tags` beacon
* v2: Comply with sorting system hierarchies for reading actual file creation time and writing it to the alias file's name


<br><br>
## Changelog
* v0.9.0: Fully functional pre-release
* v0.9.1: Added alias regeneration, improved file processing (skipping hidden files)


<br><br>
## Working principle
* Retrieving tags to process from the tags database
* Running through the directories to decipher changes (operating principle: dir size change $\Leftrightarrow$ dir change, yet not always true)
    * Or maybe can use dir edit date, if reliable? More tests needed
* Change will be compared with the contents of the '.pytags' hidden file
* Only files' tags will be accounted for by the program


<br><br>
## Instructions
* To be continued
* To display hidden files (macOS): type `defaults write com.apple.finder AppleShowAllFiles YES` in the macOS Terminal app
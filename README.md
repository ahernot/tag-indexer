# tag-indexer v2.0
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

<br>


This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.
Recursive parsing and linear algorithm (v1.0.0 was full recursive).

<br><br>
## To do
* v2.0: Add docstrings
* v2.0: Add an option to delete all beacons
* v2.0.1: Add instructions of use
* v2.1: hard-store +ALIAS and -ALIAS >> on startup, rundown this task list first to avoid missing tags in case of crash
* Add naming the file according to datetime: add a .pysorter-datetime file which acts as a datetime beacon for the current folder
* v2.1: Add an actions log (useful?)
* v2.2: Add a `case_sensitivity` setting in `preferences.py`
* v3: Only save processed tags (not in `unprocessed_tags_list`) to the `.pytags_tags` beacon
* v3: Comply with sorting system hierarchies for reading actual file creation time and writing it to the alias file's name


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


* Never manually add or delete alias files

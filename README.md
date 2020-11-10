# tag-indexer v0.1

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.


<br><br>
## To do
* Unify the docstrings and file formatting (module imports, …)
* Check that the tags beacons work correctly
* Add tag-specific processing (will only create aliases for new tags)
* Add alias deletion according to missing files from the beacons (if no beacon, delete all and recreate all)
* Program tag folder processing (with the `%`, etc.)
* v2: Add a `case_sensitivity` setting in `preferences.py`


<br><br>
## Changelog
* Nothing to show


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
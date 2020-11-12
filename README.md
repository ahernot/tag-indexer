# tag-indexer v0.1

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.


<br><br>
## To do
* Unify the docstrings and file formatting (module imports, …)
* Clean up the `preferences.py` file
* Check that the tags beacons work correctly
* v1.1: Add live time estimates, to be integrated in `indexing_functions.py`
* v2: Add a `case_sensitivity` setting in `preferences.py`
* v2: Comply with sorting system hierarchies for reading actual file creation time


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
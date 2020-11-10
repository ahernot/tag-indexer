# tag-indexer v0.1

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.


<br><br>
## To do
* Unify the docstrings and file formatting (module imports, …)
* Add a `.pytags_tags` everywhere there is a FILE (not a dir), to compare lists of tags
    * `beacons.py` will become `beacons_size.py` and create a new `beacons_tags.py` file for these tag beacons
    * During processing, choose to ignore seemingly size-unmodified folders and go deeper to the actual files
    * If the list of tags matches the `.pytags_tags` file, then skip iteration and DELETE OLD ALIASES
    * Else, create aliases
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
* To display hidden files (macOS): type `defaults write com.apple.finder AppleShowAllFiles YES` in the macOS `Terminal.app` app
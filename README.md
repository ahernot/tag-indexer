# tag-indexer v2.0.2
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

<br>

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.
Recursive parsing and linear algorithm (v1.0.0 was full recursive).

<br>

## To do
* v2.0.3: Add progress indicator and milestone cues ("Done parsing", …)
* v2.0.3: Add implementation of '.pytags-skipdir' beacon to skip parsing a directory
* v2.0.3: Add runtime deltatime calculation and logging in log.txt
* v2.0.3: Add instructions of use
* v2.0.3: Add folder reading option in main.py which reads yearmonth from folder hierarchy and adds it in alias_dirpath_rel: generate_alias_relpath()
* v2.0.3: Implement `cleaner.clean_dir` function
* v2.1: Add an option to modify the aliases' file creation datetimes to match their liked files', in `tag_processer.add_aliases`
* v2.2: hard-store +ALIAS and -ALIAS >> on startup, rundown this task list first to avoid missing tags in case of crash
* v2.2: Add naming the file according to datetime: add a .pysorter-datetime file which acts as a datetime beacon for the current folder
* v2.3: Add an alias SQL database to save the paths to (equivalent to the alias file system), and add file hyperlink generation for a query

<br>

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

* Use `cleaner.remove_beacons` function to remove all the beacon files from a directory and its subdirectories


### Beacons
`.pytags-beacon`: references all files in a directory, with their tags. JSON format
`.pytags-skipdir`: (NOT IMPLEMENTED) skip parsing of a directory and its subdirectories

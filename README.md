# tag-indexer v0.0

This is a macOS platform-specific program designed to permanently alias (using the Unix aliasing method) files according to their tags.



## To do
* New file indexing function to return a hierarchised dictionary of all directories and files, for selective processing
* The rest of the program, too
* v2: Create a '.pytags' hidden file in each directory to reference the files/tags



## Changelog
* Nothing to show



## Working principle
* Retrieving tags to process from the tags database
* Running through the directories to decipher changes (operating principle: dir size change $\Leftrightarrow$ dir change, yet not always true)
    * Or maybe can use dir edit date, if reliable? More tests needed
* Change will be compared with the contents of the '.pytags' hidden file
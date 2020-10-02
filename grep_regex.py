# grep command is used to filter the lines out of a file, and we can do this by having a variable named line (to represent the current line of some file), also the regular expression library 're' is imported. We will use this to filter out the name of the author of a book. 
# Sample input : opening a text file: truthful-living.txt
# some lines of the book : 
# Title: Beowulf
#        An Anglo-Saxon Epic Poem, Translated From The Heyne-Socin Text
# Author: Lesslie Hall
# Release Date: July 19, 2005 [EBook #16328]
# Language: English
# Character set encoding: ISO-8859-1
# Sample output : 
# Author: Lesslie Hall
re.findall('Author:.*', line)

# grep command is used to filter the lines out of a file, and we can do this by having a variable named line (to represent the current line of some file), we will use this technique to find the first name of the author of a book (we assume the name of the author is mentioned is the book)and also the regular expression library 're' is imported.
re.findall('Author:.*(\S+)', line)

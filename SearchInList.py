# returns the indices (as a list) of a chosen value in a list
# lst is the list, where search is the value to search for
# INPUT: lst = [1, 4, 8, 10, 4] and search = 4 -- OUPUT: [1, 4]
indices = [i for i in range(len(lst)) if lst[i] == search]
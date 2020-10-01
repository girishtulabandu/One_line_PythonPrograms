#Simple and Elegant Python one-liner to flatten a 2 dimensional matrix
#Suppose there is a 2D matrix- [[1, 2], [3, 4], [5, 6]]
# It will be turned into a 1-dimensional array ,ie. prints [1, 2, 3, 4, 5, 6]

ls = [[1, 2], [3, 4], [5, 6]]print([i for j in ls for i in j]) 

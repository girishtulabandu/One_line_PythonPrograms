# This python one-liner takes two list and returns a single list 
# containing sum of elements index wise i.e. new_list[0] = list1[0] + list2[0], and so...
# input: list1 = [1, 2, 3, 4, 5], list2 = [10, 11, 12, 13, 14] 
# output: [11, 13, 15, 17, 19]

new_list = list(map(lambda x,y:x+y,range(1,6),range(10,16))

'''
Number Tree Printing
Input:
number_pattern(5)

Output:
1
22
333
4444
55555
'''
num_pat = lambda x: '\n'.join(str(int(((pow(10, i)-1)/9)*i)) for i in range(1, x+1))

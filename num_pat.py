# Number Tree Printing
num_pat = lambda x: '\n'.join(str(int(((pow(10, i)-1)/9)*i)) for i in range(1, x+1))
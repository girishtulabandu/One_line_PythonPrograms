'''
Program to generate list of prime numbers in range 1 to n

Sample input:
n = 50

Expected output:
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''
l = [i for i in range(1, n) if len([a for a in range(1, i) if i % a == 0]) == 1]

# Program to generate list of prime numbers in range 1 to n
l = [i for i in range(1, n) if len([a for a in range(1, i) if i % a == 0]) == 1]

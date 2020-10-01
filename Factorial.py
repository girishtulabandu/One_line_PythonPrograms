#program for finding factorial of a number
Factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1)) 

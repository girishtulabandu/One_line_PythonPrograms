#program for checking if a number is a prime. Eg: number = 83  > prime = True
prime = all(number % i for i in range(2,number))

//Factorial program
def factorial(num):
    return 1 if num <=1 else num*factorial(num-1)
    
print factorial(1)

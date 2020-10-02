# one line code to find multiples of 2 , 3 , 5 between the range 1 to 100 using map , lambda and join function.
# Generalized form
# print("".join(map((lambda x: (str(x)+" Multiple of num1\n") if x%num1==0 else str(x)+" Multiple of num2\n" if x%num2==0 else ""),[x for x in range(start, end+1)])))
print("".join(map((lambda x: (str(x)+" Multiple of 2\n") if x%2==0 else str(x)+" Multiple of 3\n" if x%3==0 else str(x)+" Multiple of 5\n" if x%5 ==0 else ""),[x for x in range(1,101)])))

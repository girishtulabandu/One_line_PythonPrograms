# Generalized form
# one line code to find numbers between start to end having num1 , num2 or num3 as its factors using map , lambda and join function.
# print("".join(map((lambda x: (str(x)+"\n") if x%num1==0 else str(x)+"\n" if x%num2==0 else str(x)+"\n" if x%num3 ==0 else ""),[x for x in range(start,end+1)])))
# one line code to find numbers between 1 to 100 having 2 , 3 or 5 as its factors using map , lambda and join function.
print("".join(map((lambda x: (str(x)+"\n") if x%2==0 else str(x)+"\n" if x%3==0 else str(x)+"\n" if x%5 ==0 else ""),[x for x in range(1,101)])))

#one-line program to count total set bits from 1 to n
x=sum(bin(i).count('1') for i in range(n))

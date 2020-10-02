# Python one-liner to print the value of pi
# input: no input required
# output: 3.1410951411827663

value_of_pi = 4*sum((-1.0)**(n%2) / (2*n + 1) for n in range(2010))

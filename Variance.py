'''
Receives a list and returns its variance
e.g.
Input: [-1, 0, 1, 0.5, 0.3]
Output: 0.4424
'''
Var = lambda x: sum( [(xi - sum( xj for xj in x )/len(x) )**2 for xi in x] )/len(x)
# Receives a list and returns its variance
Var = lambda x: sum( [(xi - sum( xj for xj in x )/len(x) )**2 for xi in x] )/len(x)
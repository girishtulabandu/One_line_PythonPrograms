# Powerset (Set Of All Subsets) Finder. Input --> List
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def primes(x):
  return [i for i in range(2,x) if 0 not in [i%j for j in range(2,i)]]

print(primes(30))
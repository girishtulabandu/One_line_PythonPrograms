// The one-liner uses the reduce function to remove, one step at a time,
//all “marked” numbers from the initial set of all numbers between 2 and n (in the one-liner: set(range(2, n))).
// It takes this set as the initial value for the set of unmarked values r because initially, all values are unmarked.
// Now it goes over all numbers x between 2 and the square root of n (in the one-liner: range(2, int(n**0.5) + 1)) and 
// removes the multiples of x from the set r (starting at x**2) – but only if the number x is a prime number 
//(i.e., it is not removed from the set r at this point in time).


lambda n: reduce( (lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))

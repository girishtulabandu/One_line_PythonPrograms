# The program filters the multiples of 5 from the entered numbers and outputs the multiples as a single list.

list(filter(lambda x: int(x) % 5 == 0, input("Enter the numbers: ").split()))

# Sample Input: 12 23 15 20 26 25 45 29 50
# Sample Output: ['15', '20', '25', '45', '50']

#Count the number of 1s in a positive number. Example 15 [binary representation- 1111] will return 4 since it has 4 set bits.
counts = bytes(bin(x).count("1") for x in range(256))

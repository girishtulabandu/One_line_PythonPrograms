#To count the number of 1s in a number. Example- 15 [1111] has 4 1s in it.
counts = bytes(bin(x).count("1") for x in range(256))

#Program for converting decimal to binary
decimal = sum(int(bit) * 2**rank for rank, bit in enumerate(reversed(binary)))

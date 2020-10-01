# Decode string written in Hex, prints GNU's Not Unix
print(''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2)))
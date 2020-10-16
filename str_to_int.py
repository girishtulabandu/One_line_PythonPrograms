#extract number from string
#Input : 'xd3&d29g8@!bx ods0'
#output: 32980
number = int(''.join(list(filter(str.isdigit,string))))
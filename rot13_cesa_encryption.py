def o(s):return''.join([chr(ord(n)+(13if'Z'<n<'n'or'N'>n else-13))if n.isalpha()else n for n in s])
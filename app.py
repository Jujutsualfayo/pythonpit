def uppercase(str):
    for c in str:
        uppercase_char = chr(ord(c) -32) if "a" <= c <= "z" else c
        print(uppercase_char, end="")
    print()
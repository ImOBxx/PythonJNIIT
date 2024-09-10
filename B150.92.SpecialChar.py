n = input ("Enter Characters: ")
if n.isalnum():
    print("The Characters are Alphanumeric.")
elif n.isalpha():
    print("The Characters are Alphabets.")
elif n.isdecimal():
    print("The Characters are Decimals.")
elif n.isdigit():
    print("The CHaracters are Digits.")
elif n.isascii():
    print("The Characters are ASCII Values.")
elif n.isnumeric():
    print("The Characters are Numeric.")
else:
    print("The Characters Are Special Characters.")
print()
a = int (input ("Enter Numerator: "))
b = int (input ("Enter Denominator: "))
try:
    x = a / b
    print(x)
except:
    print("Denominator Should Not Be Zero.")
finally:
    print("Try Again")
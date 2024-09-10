a = int (input ("Enter 1st Number:  "))
b = int (input ("Enter 2nd Number:  "))
c = int (input ("Enter 3rd Number:  "))
if b < a and a < c:
    print(a)
elif c < a and a < b:
    print(a)
elif c < b and b < a:
    print(b)
elif a < b and b < c:
    print(b)
elif b < c and c < a:
    print(c)
elif a < c and c < b:
    print(c)

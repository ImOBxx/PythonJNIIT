n1 = int (input ("Enter Number 1: "))
n2 = int (input ("Enter Number 2: "))
n3 = int (input ("Enter Number 3: "))
x = n1 + n2 + n3
if n1 == n2:
    x = 0
    print("Sum: ", x)
elif n2 == n3:
    x = 0
    print("Sum: ", x)
elif n3 == n1:
    x = 0
    print("Sum: ", x)
else:
    x = n1 + n2 + n3
    print("Sum: ", x)


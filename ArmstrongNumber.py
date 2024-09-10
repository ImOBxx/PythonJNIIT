print()
n = int (input ("Enter Number: "))
print()
sum = 0
temp = n

while (n > 0):
    r = n % 10
    sum = sum + (r * r * r)
    n = n  // 10
if (temp == sum):
    print ("The Number Is An Armstrong Number. ")
    print()
else:
    print ("The Number Is Not An Armstrong Number.")
    print()
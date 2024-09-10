n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
if n2 > n1:
    n1, n2 = n2, n1
while n2 != 0:
    remainder = n1 % n2
    n1 = n2
    n2 = remainder
print("The GCD is:", n1)

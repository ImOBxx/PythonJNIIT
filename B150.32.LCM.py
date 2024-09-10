n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
if n1 < n2:
    n1, n2 = n2, n1
a, b = n1, n2
while b != 0:
    remainder = a % b
    a = b
    b = remainder
gcd = a
lcm = abs(n1 * n2) // gcd
print("The LCM is:", lcm)

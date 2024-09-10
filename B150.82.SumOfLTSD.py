print()
l = []
n = (int (input ("Enter List Length: ")))
print()
for i in range(1, n + 1):
    x = int (input("Enter List Values: "))
    l.append(x)
print()
print(l)
print()
sum = 0
for i in l:
    sum = sum + i
print("Sum: ", sum)
print()
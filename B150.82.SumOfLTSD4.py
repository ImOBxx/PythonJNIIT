n = int (input ("Enter Dictionary Length: "))
l = []
a = []
for i in range(1, n + 1):
    x = input("Enter Keys: ")
    l.append(x)

for i in range(1, n + 1):
    b = int (input ("Enter Values: "))
    a.append(b)

t = dict(zip(l, a))
sum = 0
for keys, values in t.items():
    sum = sum + values
print("Sum Of Dictionary [Values] : ", sum)

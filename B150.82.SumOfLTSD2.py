x = []
n = int (input ("Enter List Length: "))
for i in range(1, n + 1):
    l = int (input ("Enter List Values: "))
    x.append(l)
t = tuple(x)
print(t)
sum = 0
for i in t:
    sum += i
print("Sum Of Tuples: ", sum)


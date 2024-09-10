n = int (input ("Enter List Length: "))
x = []
s = []
for i in range(n):
    l = int (input ("Enter List Values: "))
    x.append(l)
x.pop(0)
print(x)
    
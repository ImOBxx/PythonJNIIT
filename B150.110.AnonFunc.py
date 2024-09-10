l = []
n = int (input ("Enter List Length: "))
for i in range(n):
    x = int (input ("Enter List Values: "))
    l.append(x)
s = []
print(l)
for i in l:
    if i % 15 == 0:
        s.append(i)
print(s)



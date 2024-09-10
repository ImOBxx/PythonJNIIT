n = int (input ("Enter List Length: "))
x = []
for i in range(n):
    l = int (input ("Enter List Values: "))
    x.append(l)
print(x)
sum = 1
for i in x:
    sum = sum * i
print("Product Of List: ", sum)



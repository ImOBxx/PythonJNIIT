A= []
for x in range (2, 10, 2):
    A.append(x)
print(A)

x = "hello world"
print(list(x))

a = list(x)
a[4] = "u"
print(a)
a[4] = "u"
print(a)
y = " ".join(a)
print(y)



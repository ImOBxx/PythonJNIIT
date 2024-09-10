n = "Abhishek Here"
x = n.split()
d = "Is"
if x[0] != "Is":
    x.insert(0, "Is")
    j = ' '.join(x)
    print(j)
else:
    print(n)

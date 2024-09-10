n = input ("Enter Text: ")
x = n.split()
d = {}
for i in x:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
print(d)



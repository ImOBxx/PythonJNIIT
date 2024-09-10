a = [1, 2, 3, 7, 2, 1, 5, 6, 4, 8, 5, 4]
dup = set()
uniq = []
for x in a:
    if x not in dup:
       uniq.append(x)
       dup.add(x)
print(uniq)
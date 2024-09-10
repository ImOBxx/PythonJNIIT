c1 = set(["White", "Black", "Red"])
c2 = set(["Red", "Green"])
dup = set()
for i in c1:
        if i not in c2:
            dup.add(i)
print(dup)
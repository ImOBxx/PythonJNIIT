print()
n = int (input ("Enter List Length: "))
print()
x = []
for i in range(n):
    l = int (input ("Enter List Values: "))
    x.append(l)

print()
d = int (input ("Enter Nth Term: "))
print()
for i in x:
    if d < i:
        print("All Numbers in the List are Greater Than The Nth Term. ")
        print()
        break
    else:
        print("All Numbers in the List are Not Greater Than The Nth Term. ")
        print()
        break



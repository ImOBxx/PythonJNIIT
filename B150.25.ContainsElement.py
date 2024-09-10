print()
l = []
for i in range(1, 6):
    n = int (input ("Enter Number: "))
    l.append(n)
print()
print(l)
x = 3
print()
print("Specified Value: ", x)
print()
if x in l:
    print("Specified Value Is In The List.")
    print()
else:
    print("Specified Value Is Not In The List.")
    print()

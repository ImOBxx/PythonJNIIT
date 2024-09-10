print()
n = int (input ("Enter Factorial Number: "))
print()
f = 1
d = {}
print(f"Dictionary Of Factorial Till {n} :- ")
print()
for i in range (1, n + 1):
    f = f * i
    d[i] = f
print(d)
print()




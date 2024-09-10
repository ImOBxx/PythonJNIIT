l = []
count = 0
print()
for i in range(1, 6):
    n = int (input ("Enter Number: "))
    l.append(n)
print()
print(l)
print()
for i in l:
    if i == 4:
       count += 1     
print("Count Of 4's In The List: ", count)
print()
n = int (input ("Enter List Length: "))
x = []
d = []
for i in range(n):
    l = int (input ("Enter Number: "))
    x.append(l)
for i in x:
    if i not in d:
        d.append(i)
if x == d:
    print("The Numbers are Different From Each Other. ")
else:
    print("There Are Same Elements In The List. ")

    
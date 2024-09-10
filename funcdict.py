#arbitery keyword argument
def add(**a):
    print(a)
    for i in a.values():
        sum = sum + i
    print (sum)

add(x = 5, y = 8, z = 9, e = 8, h = 12)


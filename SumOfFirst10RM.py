sum = 0
def first (start, end):
    global sum
    if start <= end:
        print(start)
        sum = sum + start
        first(start + 1, end)
    return (sum)

s = first(1, 10)
print("Sum: ", s)

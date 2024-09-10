sum = 0
def make(start, end):
    global sum
    if start <= end:
        print(start)
        sum = sum + start
        make(start + 1, end)
        return (sum)


s = make(1, 10)
print("Sum: ", s)
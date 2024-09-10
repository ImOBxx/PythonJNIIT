sum = 0
def make (x, y):
    global sum
    if x <= y:
        print(x)
        sum = sum + x
        make (x + 2, y) 
        print(sum)
    
s = make(0, 10)
print("Sum: ", s)
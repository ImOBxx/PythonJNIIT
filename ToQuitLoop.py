sum = 0
count  = 0
while (True):
    x = int (input("Enterc Number: "))
    if x == 0:
        print ("Total Sum Of Numbers is ", sum)
        break
    else:
        sum = sum + x
        count = count + 1

print ("Average Of Value is: ", sum / count)
sum = 0
count = 0
while (True):
    x = int (input ("Enter a Number: "))
    if x == 0:
        sum = sum + x
        print ("Number is Zero")
        print ("The Total SumOf Numbers is: ", sum)
        break
    else:
        count += 1
print ("Average Of Values Is: ", sum / count)
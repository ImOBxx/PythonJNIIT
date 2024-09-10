x = int (input ("Enter a Number: "))
temp = x
count = 0
while temp > 0:
    temp = temp // 10
    count = count + 1

print ("Number of Digits in ", x, " is ", count)
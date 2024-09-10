n = int (input ("Enter Number: "))
x = int (input ("Enter Digit To Search: "))
count = 0
temp = n
while (temp > 0):
    rem = temp % 10
    if rem == x:
        count = count + 1
    else:
        temp = temp // 10

print ("The Number ", n, " digit ", x, " is found ", count, " times ")

xxxxxxxxx
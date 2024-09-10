x = int (input ("Enter a Number: "))
count = 0
sum = 0
while (x > 0):
    r = x % 10
    sum = sum + r
    print (r, end = " ")
    x = x // 10

    if (r == 1 or r == 2 or r == 3 or r == 4 or r == 5 or r == 6 or r == 7 or r == 8 or r == 9 or r == 10):
      count += r
      print (count, end = "")
    else:
       print (end = "")


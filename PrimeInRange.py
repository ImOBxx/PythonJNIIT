x = int (input ("Enter Statring Point: "))
y = int (input ("Enter Ending Point: "))
c = 1
count = 0
for i in range (x, y + 1):
    c = c + 1
    if c % i == 0:
        count = count + 1

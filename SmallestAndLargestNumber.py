numbers = []
for i in range (1, 11):
    n = int (input ("Enter Number: "))
    numbers.append(n)
smallest = min (numbers)
largest = max (numbers)
print ("The Smallest Number Is: ", smallest)
print ("The Largest Number Is: ", largest)
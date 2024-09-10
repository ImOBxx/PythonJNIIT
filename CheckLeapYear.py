y = int (input("Enter Year: "))
if (y % 4 == 0 and y % 400 == 0 and y % 100 == 0):
    print ("Leap Year.")
else:
    print ("Not a Leap year.")
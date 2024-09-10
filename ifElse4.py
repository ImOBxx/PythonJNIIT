per = int (input ("Enter Percentage: "))
if (per <= 100 and per >= 80):
    print ("A Grade.")
elif (per <= 79 and per >= 60):
    print ("B Grade.")
elif (per <= 59 and per >= 50):
    print ("C Grade.")
elif (per <= 35 and per >= 49):
    print ("D Grade.")
elif (per <= 35 and per >= 0):
    print ("Fail.")

s = input ("Enter String: ")
x = list(s)
for i in x:
    if i.islower():
        print("There is a Lower Case Letter.")
        break
    else:
        print ("There is no Lower Case Letter.")
        break


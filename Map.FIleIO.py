m = [58, 74, 90]
name = ["Akash", "Vaibhav", "Ramesh"]
def per(a):
    return (a * 10) / 100.0






# ml = [i for i in map(per, m)] #Zip Method
ml = [i for i in map(lambda a: (a * 10) / 100.0, m)] #Lambda Expression
print(ml)

nl = [name for name in map(lambda x: x.upper(), name)]
print(nl)

#map Create Function
#lambda create no function

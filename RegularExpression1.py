import re
pattern=re.compile("[a]{2}")

matchObject=pattern.match("aaHeaallo a")

if(matchObject):
    print(matchObject.group())
    print(matchObject.span())
    print(matchObject.start(),matchObject.end())
else:
    print("Not Found")


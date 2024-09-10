"""
Raising Exceptions in  Python
To Throw an Exception if certain condition are met.
it allows you to interrupt the program based on your requirement.


To trow an Exception, we have to use the raise keyword 
followed by an Exception name.

"""

def checkAge(age):
    if age<18:
        #raise ValueError
        raise ValueError("Please Enter valid age.")    
    else:
        print("Congratulations! Your age is Valid")

try:
 checkAge(10)
except Exception as e:
   print(e)

   
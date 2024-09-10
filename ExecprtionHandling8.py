a = [10, 20, 30, 40]
try:
    print("Second Element: ", a[1])
    print("Fifth Element: ", a[4])

except:
    print("Index Error")
#or

def fun(a):
    if a < 4:
        b = a / (a - 3)
        print("Value Of b = ", b)
    
try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("Division Error Occured")

except NameError:
    print("Name Error")




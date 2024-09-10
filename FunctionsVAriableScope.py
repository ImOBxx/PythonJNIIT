a = 5 #Global Variable

def abc():
    global a
    a = 10 # Local Variable O = 10; 

abc()

print(a)


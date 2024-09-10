class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __sub__ (self, other):
        return self.age + other.age
    
e1 = Employee ("Akash", 20)
e2 = Employee ("Akash", 30)
print(e1 + e2)


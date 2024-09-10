class Person:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add

    def __str__(self):
        return ("\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Address: {self.add}\n"
                "\n")
print()
name = input ("Enter Name: ")
age = (int (input("Enter Age: ")))
add = input ("Enter Address: ")
print()

s1 = Person(name, age, add)
print(s1)            
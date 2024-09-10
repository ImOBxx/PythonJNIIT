class Student:
    
    def __init__(self, name, city, marks):
        print("Object Created")
        self.name = name
        self.city = city
        self.marks = marks


s1 = Student("Akash", "Lucknow", [58, 89, 74])

print(s1.name, s1.city)
s1.name = "Ramesh"
print(s1.name)


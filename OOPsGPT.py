class Student:    
    def __init__(self, name, city, marks):
        self.name = name
        self.city = city        
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

# Main program
s1 = Student("Akash", "Lucknow", [58, 89, 74, 38, 48, 45])  # Object creation or instantiation

print("Total Marks:", s1.total_marks())
print(s1.name, s1.city)
s1.name = "Ramesh"
print(s1.name)

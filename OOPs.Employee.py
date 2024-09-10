class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def printName(self):
        print(self.name)

class Employee(Person):
    def __init__(self, name, age, salary, post):
        super().__init__(name, age)
        self.salary = salary
        self.post = post

    def display(self):
        print()
        super().display()
        print(f"Salary: {self.salary}")
        print(f"Post: {self.post}")
        print()


e1 = Employee("Rahul Kumar", 23, 837673, "Intern")
e1.display()


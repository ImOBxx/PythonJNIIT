class Employee:
    "Hello This is Employee Class"
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        #return "Name:"+self.name+", Age:"+str(self.age)+", City: "+self.city
        return (f"\n"
                f"Name: {self.name}\n" 
                f"Age: {self.age}\n"
                f"City: {self.city}\n")
        #eturn "Name: {0}, Age: {1}, City: {2}".format(self.name,self.age,self.city)
    
print()
name = input("Enter Name: ")
age = int (input ("Enter Age: "))
city = input("Enter City: ")
print()

e1 = Employee(name, age, city)

print(e1)



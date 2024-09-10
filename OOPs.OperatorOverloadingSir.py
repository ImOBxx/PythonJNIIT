class Employee:
    def init(self,name,age):
        self.name=name
        self.age=age  

    def str(self):
        return f"[Name: {self.name},Age:{self.age}]" 
     
    def add(self,other):
        return self.age+other.age


empList=[]

while True:
    name=input("Enter Employee Name:\n")
    age=int(input("Enter Employee age:\n"))
    e=Employee(name,age)
    empList.append(e)
    choice=input("Do You want to continue press y otherwise press n")
    if choice!="y":
        break

for emp in empList:
    print(emp)
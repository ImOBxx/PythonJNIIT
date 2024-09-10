class Student:    
    """def init(self,name,city,marks):
        self.name=name
        self.city=city        
        self.marks=marks"""
    def total_marks(self):
        sum=0
        for m in self.marks:
            sum+=m
        print("Total Marks is :", sum)

#main Program

s1=Student("Akash","Lucknow",[58,89,74,38,48,45]) #object creation or instantiation


s1.total_marks()

print(s1.name,s1.city)
s1.name="Ramesh"
print(s1.name)
class Base:
    def init(self):
        self.a="Hello" #public variable
        self.__c="Good Morning" #private variable
    
    def setC(self,c):
        self.__c=c
        
    def getC(self):
        return self.__c


obj=Base()

obj.a="bye"
obj.setC("Good Evening")
print(obj.getC(),obj.a)


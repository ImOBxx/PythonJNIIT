class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self):
        return self.a + self.b
    
    def __str__(self):
        return (f"Sum Of The 2 Numbers: {self.compute()}")

print()   
a = int (input ("Enter Number 1: "))
b = int (input ("Enter Number 2: "))
print()
s1 = Add(a, b)
print(s1)


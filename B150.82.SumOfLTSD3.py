n = int (input ("Enter Set Length: "))
s = set()
for i in range(1, n + 1):
    l = int (input ("Enter Set Values: "))
   
    s.add(l)
print(s)
sum = 0
for i in s:
    sum += i
print("Sum: ", sum)
    

    

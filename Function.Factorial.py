def factorial(n):
    
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int (input ("Enter Number: "))
print(f"The Factorial Of {n} is: ", (factorial(n)))



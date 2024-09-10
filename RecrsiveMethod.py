def greet(n):
    if n > 0:
     print("Hello")
     greet(n - 1)

greet(5)
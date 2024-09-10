for x in range(1, 100):
    if x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    elif x % 3 == 0 & x % 5 == 0:
        print("Fizz Buzz", end = " ")
    else:
        print(x)

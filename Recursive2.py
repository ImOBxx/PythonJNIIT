sum=0
def greet(start, end):
    global sum
    if start <= end:
        print(start)
        sum=sum+start
        greet(start + 1, end)
    return(sum)    

s=greet(1, 10)  
print("sum:",s)
                                                  
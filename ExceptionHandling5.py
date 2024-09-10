try:
    mylist=[10,20,30,40]
    print(mylist[9])
except Exception as e:
    print(e)
else:
    print("Code Executed Successfully")
finally:
    print("Code Execution Finished")
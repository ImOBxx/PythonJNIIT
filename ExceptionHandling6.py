try:
    print()
    f = open('testfile.txt')
    raise FileNotFoundError
except FileNotFoundError:
    #print(e)
    print("Sorry, This File Doesn't Exist.")
except Exception:
    #print(e)
    print("Sorry, Something went wrong.")

else:
    print(f.read())
    f.close()
finally:
    print("Execution Finally...")

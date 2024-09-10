# r = read mode
# w : write mode
# a : append mode

fileObj = open("Stuname.txt","r")
para = ["Hello\n", "Hi"]
fileObj.writelines(para)
for i in range(50):
  fileObj.write("Ramesh\n", i)



fileObj.close()







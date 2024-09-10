import numpy as np


x=np.array([10,20,30,40,50])

print(x)
print("Number of Dimension:",x.ndim)
print("Total Number of Elements:",x.size)
print("Shape of Array:",x.shape)
#add element
x=np.append(x,8) #x is an array,8 is a value
print(x)
#delete element
x=np.delete(x,2) #x is an array, 2 is an index number
print(x)
#sort numpy array
x=np.sort(x)
print(x)

import numpy as np

x=np.arange(5)

print(x)

x=np.arange(1,11)
print(x)

x=np.arange(1,51,3)
print(x)

import numpy as np

x=np.array([[10,20,30],[40,50,60]])
print(x)
print("Number of Dimension:",x.ndim)
print("Total Number of Elements:",x.size)
print("Shape of Array:",x.shape)
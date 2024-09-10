import numpy as np

x=np.array([10,20,30,40.5])

#upcasting feature in numpy array
print(x)#[10.  20.  30.  40.5]

print(type(x))
print(x.dtype)

#creating array from scratch
import numpy as np

#zeros
x=np.zeros(5,dtype='int32')
print(x)
x=np.zeros((2,3),dtype='int32')
print(x)

#ones
x=np.ones(10,dtype=float)
print(x)

x=np.ones((4,3),dtype=float)
print(x)

#full with specific value
x=np.full((3,3),100)
print(x)

x = np.full
def sum(a,b):
     return a+b
L1=[-1,9,3]
L2=[5,6,7]  
L=[ x for x in map(min, L1, L2) ]
print(L)

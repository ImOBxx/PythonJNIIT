import pandas as pd
import numpy as np

print(pd.__version__)

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(type(data))

print(data.values)

print(data.index)

print(list(data.index))

print(data[1])

print(data[1:3])

data = pd.Series([0.25, 0.5, 0.75, 1.0],
       index=['a', 'b', 'c', 'd'])


print(data[0])

print(data.iloc[0])

print(data["c"])

print(data.c)

data2 = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index = [2, 5, 3, 7])
print(data2)

print(data2[5])

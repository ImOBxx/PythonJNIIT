import numpy as np

x = np.array([10, 20, 30, 40])

f = np.split(x, [2])

print(f)

grid = np.arange(16).reshape(4, 4)

print(grid)

a = np.vsplit(grid, [1, 2, 3])

print(a)

b = np.hsplit(grid, [1, 2, 3])

print(b)
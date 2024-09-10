import numpy as np
x = np.random.randint(10, size=(3, 4))

print(x)
print(x<5)
print(x[x<5])
print(np.count_nonzero(x<5))
print(np.sum(x<5))
#how many values less than 5 in each row?
print(np.sum(x < 5, axis=1))
#how many values less than 5 in each column?
print(np.sum(x < 5, axis=0))
# are there any values greater than 8?
print(np.any(x > 8))
# are there any values less than zero?
print(np.any(x < 0))
# are all values less than 10?
print(np.all(x < 10))
# are all values equal to 6?
print(np.all(x == 6))
#are all values in each row less than 8?
print(np.all(x < 8, axis=1))

print(bool(56))#True
print(bool(""))#False
print(bool("False"))#True

print(bool(54 & 0))#False

print(int("111",2))#binary to decimal
print(int("0xFD3",16))#hexadecimal to decimal
print(int("546",8))#Octal to decimal

print(bin(7))#decimal to binary

import numpy as np
import pandas as pd

rainfall=pd.read_csv(r"Seattle2014.csv")['PRCP'].values
inches = rainfall / 254 # 1/10mm -> inches

print("Number days without rain: ", np.sum(inches == 0))
print("Number days with rain: ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches :", np.sum((inches > 0) &
(inches < 0.2)))

#construct a mask of all rainy days
rainy = (inches > 0)
print(rainy)

# construct a mask of all rainy days
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

print("Median precip on rainy days in 2014 (inches): ",
np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ",
np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
np.median(inches[rainy & ~summer]))





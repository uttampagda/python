from array import *

a = array('I', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# creating an array with float type
b = array('d', [2.5, 3.2, 3.3])

# printing original array 1
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
    print(b[i], end=" ") # second time print array

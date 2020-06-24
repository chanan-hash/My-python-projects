from numpy import *

arr1 = array([
             [1,2,3],
             [4,5,6]
                ])

arr2 = arr1.flatten()

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr2)
print(id(arr2))
print(id(arr1))



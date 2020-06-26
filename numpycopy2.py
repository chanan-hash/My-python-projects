from numpy import *

arr1 = array([2,6,8,1,3])

arr2 = arr1.copy()

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

for i in range(len(arr1)):
    print(arr1[i]+arr2[i],end=" ")

print()

for a,b in zip(arr1,arr2):
    print(a+b,end=" ")

print()

max = 0
for j in range(len(arr1)):

    if  arr1[j] > max:
        arr1[j] = max

print(max)

from numpy import *
#chanan hagever
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])
arr3 = arr1 + arr2

print(arr3)
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(concatenate([arr1,arr2]))

x = 0
for i in range(len(arr1)):
    arr1[i]+=5
    x+=i

print(x)
print(arr1)

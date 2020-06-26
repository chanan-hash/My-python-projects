import math
from array import *
x = int(input("Enter a number "))

print(math.factorial(x))


vals = array('i',[5,9,8,4,2])

newArr = array(vals.typecode, (a for a in vals))
newArr = sorted(newArr)
for i in range(len(newArr)):
    print(newArr[i])

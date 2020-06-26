from array import *
x = array('i',[3,5,7,8,9])

print(x)

y = array(x.typecode, (a for a in x[2]))

counter = len(x)-1

for i in x:
    y[counter] = i
    counter -=1

print(y)


z = array('i', [6,8,5,7])
for i in range(z):
    if i==2:
        pass
    else:
        print(z[i])





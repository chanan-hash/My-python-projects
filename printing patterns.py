for i in range(4):
    for j in range(4 - i):
        print(j+1+i, end='')
    print()


x = 'ABCD'
y = 'PQR'

for i in range(4):
    for k in range(i+1):
        print(x[k],end='')
    for j in range(i,3):
        print(y[j],end='')
    print()


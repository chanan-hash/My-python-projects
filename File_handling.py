
f = open('MyData','r')

#print(f.readline(), end= "")
#print(f.readline())

#f1 = open('abc','a')

#f1.write("Something ")
#f1.write("people")
#f1.write(' Moblie')

f1 = open('abc','w')

#for data in f:
#   print(data)

for data in f:
    f1.write(data)

f2 = open('IMG_6309.JPG', 'rb')

f3 = open('MyPic.JPG','wb')

#for i in f2:
#    print(i)

for i in f2:
    f3.write(i)

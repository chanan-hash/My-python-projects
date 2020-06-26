
av = 10

x = int(input("How mant candies you want? "))

i = 1
while i<=x:
    if i> av:
        print("Out of stock")
        break

    print("Candy")
    i += 1

print ("Bye")


for i in range(1,100):
    if i % 3==0 or i % 5==0:
        continue
    print(i)


for i in range(101):
    if i % 2!=0:
        pass
    else:
         print(i)


# fibonacci
a = 0
b = 1
for i in range(0,48):
    c = a+b
    print(c)
    a = b
    b = c

# prime/not prime
x = int(input(" enter a number: "))
if (x ==2):
    print("prime")
else:
    for i in range(2,x):
        if (x % i == 0):
            print("not prime")
            break
        else:
            print("prime")
            break


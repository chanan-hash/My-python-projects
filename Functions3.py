
def person (name,age=18):
    print(name)
    print(age)

person('chanan',21)

def sum(*b):

    print(b)
    c = 0

    for i in b:
        c = c + i

    print(c)

sum(5.5,6,34,78)


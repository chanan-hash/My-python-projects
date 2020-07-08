
def person(name,**data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)

person('chanan', age = 21,city = 'PT',mob =1234567890)

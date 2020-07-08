
def count (lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even += 1
        else:
            odd += 1
    return even,odd

lst = [20,25,14,19,16,24,28,47,26]

even, odd = count(lst)
print("Even: {} and Odd: {}".format(even,odd))


def user(names):
    for name in names:
        if len(name)>5:
            print(name)
        else:
            continue
    return name

names = []
for i in range(10):
    names.append(input("Enter a name: "))
print(names)

print(user(names))

# x = input("Enter a name: ")
# names.append(x)



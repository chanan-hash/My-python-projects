
#from here there are  all kind of checking I did from another course

def func(message, num=1):
    print(message * num)
func('Welcome')
func('Viewers', 3)

for i in range(1, 6):
    print(str(i) * i)

i = -10
j = 1
while i < 0:
    i += j
    j += 1
print(j)

my_dict = {(1, 2): 1, (2, 3): 2}
for key in my_dict.keys():
# printing only the keys of the dic'. the loop run on the dictionary and find the keys and printing them
    print(key)

salad_ingredients = ("tomato", "cucumber", "tuna fish", "onion")
#salad_ingredients[2] = "spinach"
print(salad_ingredients)

def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
    # Ignore the last comma.
    return output[:-2]

print(combine_coins('$',range(5)))

def magic(a, b):
    return a * b
list_one = [1, 2, -5, 6]
list_two = [2, -1, 3, 4]
print(list(map(magic, list_one, list_two)))
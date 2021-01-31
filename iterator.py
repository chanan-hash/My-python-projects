
num = [7,8,9,5]

print(num[1])


for i in num:
    print(i, end= " ")

it = iter(num)

print(it.__next__())
print(it.__next__())

print(next(it))


# השלב השני בשיעור, יצירת איטרציה עצמאית במחלקה

class TopTen:

    def __init__(self):
       # לא קשור ל num למעלה
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:

            val = self.num
            self.num +=1

            return val

        else:
            raise StopIteration

values = TopTen()

print(values.__next__())

print(next(values))

for i in values:
    print(i)


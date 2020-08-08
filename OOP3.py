
class Computer:
    def __init__(self):
        self.name = "Chanan"
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

#c1.name = "Moshe"
#c1.age = 12

c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("Thye are different")

print(c1.name)
print(c2.name)


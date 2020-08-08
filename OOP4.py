
class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.Com = "BMW"

c1 = Car()
c2 = Car()

c1 .mil = 8
Car.wheels = 5

print(c1.Com, c1.mil, c1.wheels)
print(c2.Com, c2.mil, Car.wheels)



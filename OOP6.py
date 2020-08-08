
class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand  = 'hp'
            self.cpu = 'i5'
            self.ram = 8

s1 = Student('Moshe',2,'Hp','i5',8)
s2 = Student('Jenny',3)

print(s1.name, s1.rollno)
s1.show()

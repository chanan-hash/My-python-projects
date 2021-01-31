from abc import ABC, abstractclassmethod

class Computer(ABC):
    @ abstractclassmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class Whiteboard(Computer):
    def write(self):
        print("its writing")

class Progranner:
    def work(self, com):
        print("Solving bugs")
        com.process()

#com = Computer()
com1 = Laptop()
#com1.process()
com1.process()

com2 = Whiteboard()

prog1 = Progranner()
prog1.work(com1)

prog1.work(com2)

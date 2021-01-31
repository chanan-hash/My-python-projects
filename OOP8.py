class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):

        print("in B Init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

class C (A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")

    def feat(self):
        super().feature2()


a1 = A()
b1 = B()
c1 = C()
c1.feature1()
c1.feat()

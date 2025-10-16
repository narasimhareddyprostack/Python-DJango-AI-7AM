class Test:
    def __init__(self):
        print("constructor is special method")

    def m1(self):
        print("Instance Method")

    @classmethod
    def m2(cls):
        print("class method")

    @staticmethod
    def m3():
        print("staic method")

t1=Test()
t2=Test()
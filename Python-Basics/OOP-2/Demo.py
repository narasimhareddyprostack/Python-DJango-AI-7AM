class Demo:
    a=10           #class level
    def m1(self):
        self.b=20 #instance Varaible
    @classmethod
    def m2(cls):
        cls.c=30  #class Variable
        Demo.d=40 #class Variable
    @staticmethod
    def m3():
        Demo.e=50 #class Variable

d1=Demo()
d1.f=60
d1.m1()
d1.m2()


d2=Demo()
d2.m1()
print(d1.__dict__)
print(d2.__dict__)
print(Demo.__dict__)



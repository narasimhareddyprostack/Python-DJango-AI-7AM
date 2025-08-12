class Test:
    a=100         #class level variable

    def m1(self):
        self.b=200  #instance var- using self
        self.c=300  #instance var- using self

    @classmethod
    def m2(cls):
        pass 
    @staticmethod
    def m3():
        pass

t1=Test()
t1.m1()
t1.d=400
t2=Test()
t2.m1()


print(Test.__dict__)
print("********")
print(t1.__dict__)

print(t2.__dict__)


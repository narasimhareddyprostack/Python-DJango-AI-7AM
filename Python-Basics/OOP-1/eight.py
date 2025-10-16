class Test:
    a=100           #class variable

    def m1(self):
        self.b=200 #Instance Varaible

    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        c=100     #Local varaible
        

t1=Test()
t1.m1()

print(t1.__dict__)
print(Test.__dict__)
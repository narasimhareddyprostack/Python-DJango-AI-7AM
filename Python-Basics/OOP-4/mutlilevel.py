class GP:
    def m1(self):
        print("Grand Parnet Class - m1 Method")
class Parent(GP):
    def m2(self):
        print("Parnet Class - m2 Method")
    def m3(self):
        print("Parnet Class - m3 Method")

class Child(Parent):
    def m4(self):
        print("Child Class - m4 Method")

c1=Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
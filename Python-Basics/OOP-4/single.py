class Parent:
    def m1(self):
        print("Parnet Class - m1 Method")
    def m2(self):
        print("Parnet Class - m2 Method")

class Child(Parent):
    def m3(self):
        print("Child Class - m3 Method")

c1=Child()
c1.m1()
c1.m2()
c1.m3()
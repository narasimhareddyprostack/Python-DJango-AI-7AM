class Parent1:
    def m1(self):
        print("Parent1 Class - m1 method") 
    def m2(self):
        print("Parent1 Class - m2 method") 


class Parent2:
    def m3(self):
        print("Parent2 Class - m3 method") 
    def m4(self):
        print("Parent2 Class - m4 method") 



class Child(Parent1,Parent2):
    def m5(self):
        print("Child Class - m5 method") 


c1=Child()

c1.m1()
c1.m2()
c1.m5()
c1.m3()
c1.m4()

class CEO:
    def m1(self):
        print("CEO class - m1 method") 
    def m2(self):
        print("CEO class - m2 method")

class CTO(CEO):
    def m3(self):
        print("CTO class - m3 method") 

class TL1(CTO):
    def m4(self):
        print("TL1 class - m4 method") 

class TL2(CTO):
    def m5(self):
        print("TL2 class - m5 method")
    

tl2= TL2()
tl2.m1()
tl2.m2()
tl2.m3()
tl2.m5()
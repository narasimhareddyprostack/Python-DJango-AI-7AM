class Test:
    def __init__(self):
        print("constructor is a special method")
        
    def m1(self):
        print("m1 - normal instance method")
    
    @classmethod
    def m2(cls):
        print("m2 - class method")

Test()
Test()
Test()
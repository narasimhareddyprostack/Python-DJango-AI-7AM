class Parent:
    a=100

class Child(Parent):
    pass

c1=Child()

#print(Child.__dict__)
print(c1.a)

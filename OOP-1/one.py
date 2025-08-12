class Account:
    pass

a1=Account()
a2=Account()


print(a1)
print(id(a1))
print(a1.__dict__)   #{}

print(a2)
print(id(a2))
print(a1.__dict__)   #{}
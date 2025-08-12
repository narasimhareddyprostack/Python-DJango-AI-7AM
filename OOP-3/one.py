class Account:
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount

    def open_account(self):
        print("Account Opened Successfully")
    def deposit_amount(self,amount):
        pass




a1=Account(101,"Rahul",1000)   #creating object
a2=Account(102,"Sonia",2000)   #creating object
print(a1.__dict__)
print(a2.__dict__)
a1.deposit_amount(5000)
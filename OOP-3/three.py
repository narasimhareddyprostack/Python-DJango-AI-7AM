class Account:
    min_bal=500
    branch_name="SBI Marathahalli"
    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=amount 
    def open_account(self):
        print("Accoount Opened")

    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal+amount 

    def withdrawl_amount(self,amount):
        self.acc_bal = self.acc_bal-amount 
    def get_bal(self):
        return self.acc_bal-self.min_bal
a1=Account(101,"RG",5000)
a2=Account(102,"SG",6000)
a3=Account(103,"PG",50000)
#print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
a1.deposit_amount(1500)
a2.deposit_amount(500)
a3.deposit_amount(5000)
print("********************************")
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print("********************************")

print(a1.get_bal())
print(a2.get_bal())
print(a3.get_bal())
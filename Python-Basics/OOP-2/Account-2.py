class Account:

    def open_account(self):
        print("Account Opened")
    def deposit_amount(self,amount):
        print(amount , "- Amount Deposited")
    def withdrawl(self,amount):
        print(amount," - Amount Withdrawl")
    
a1=Account()
a1.open_account()
a1.deposit_amount(5000)
a1.deposit_amount(500)
a1.withdrawl(15)
a1.withdrawl(20)
#a2=Account()
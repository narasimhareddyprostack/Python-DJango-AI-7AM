class Account:
    ''' Account Class created By Narasimha - Prostack '''
    
    min_bal=500

    def open_account(self):
        print("Account Opened Successfully")

    def deposit_amount(self):
        print("Account Deposited")
    
    def withdrawl(self):
        print("Account Withdrawl successfully")
    def get_bal(self):
        return 100

a1=Account()

print(a1.min_bal)
a1.open_account()
a1.deposit_amount()
a1.withdrawl()

acc_bal=a1.get_bal()
print(acc_bal)
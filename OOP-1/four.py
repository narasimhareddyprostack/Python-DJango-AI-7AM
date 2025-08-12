class Account:
    ''' Account Class created By Narasimha - Prostack '''
    
    min_bal=500

    def open_account():
        print("Account Opened Successfully")

    def deposit_amount():
        print("Account Deposited")


a1=Account()
print(Account.__dict__) #{"open_account":<function 4532>,"deposit_amount"}:<function > 
print(a1.__dict__)      #{}
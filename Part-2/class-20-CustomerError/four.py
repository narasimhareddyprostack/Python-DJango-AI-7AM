class InsuffientBalError(Exception):
    def __init__(self,msg):
        #print("inside constructor")
        self.msg=msg

def withdrawl(amount):
    acc_bal=500
    if acc_bal>amount:
        print("Withdrawl and Enjoy")
    else:
        #print("Insuffient Bal")
        #print(10/0)  #ZeroDivisionError
        try:
            raise InsuffientBalError("Buddy! Balance is Low")
        except InsuffientBalError as err:
            print(err)

amount=int(input("Enter amount to Withdrawl:"))
withdrawl(amount)
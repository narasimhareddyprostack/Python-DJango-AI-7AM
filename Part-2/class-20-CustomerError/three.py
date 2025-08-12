class InsuffientBalError(Exception):
    def __init__(self,msg):
        self.msg=msg


def withdrawl(amount):
    acc_bal=500
    if acc_bal>amount:
        print("Withdrawl and Enjoy")
    else:
        #print("Insuffient Bal")
        #print(10/0)  #ZeroDivisionError
        raise InsuffientBalError("Buddy! Balance is Low")


withdrawl(2000)
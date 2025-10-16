class InsuffientBalError(Exception):
    def __init__(self,msg):
        self.msg=msg



print(10/0)    #ZeroDivisionError 
#how to handle - try and except block

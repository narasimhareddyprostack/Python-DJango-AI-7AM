from abc import *
class Bank(ABC):

    @abstractmethod
    def calc(self):
        pass 


class Account(Bank):
    pass

    """ #method implementation
    def calc(self):
        pass 
 """

a1=Account()
print(Account.__dict__)
print(a1.__dict__)
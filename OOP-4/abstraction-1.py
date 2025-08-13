from abc import *
class Bank(ABC):

    @abstractmethod
    def calc(self):
        pass 


b1=Bank()
print(b1)      
print(type(b1))
print(id(b1))

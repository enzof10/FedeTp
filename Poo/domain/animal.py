from abc import ABC , abstractmethod

class animal(ABC):

    name= str
    tricks = str
    
    @abstractmethod
    
    def doTricks(self):
        pass
        
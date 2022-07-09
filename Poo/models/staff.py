from abc import ABC , abstractmethod

class Staff(ABC):

    speciality= str
    workTime = str
    salary= float 

    @abstractmethod
    
    def work(self):
        pass

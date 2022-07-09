import logging
from models.staff import Staff

class Trainer(Staff):

    def __init__(self, speciality,workTime,salary):
        self.__speciality = speciality
        self.__workTime = workTime
        self.__salary = salary
    
    def __str__(self):
        return f" Specializated in {self.__speciality} \t Worktime: {self.__workTime} \t Salary:{self.__salary}"

    def work(self):
        logging.info("training and teaching tricks to animals") 

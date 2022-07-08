import logging
from mimetypes import init
import webbrowser
from domain.animal import animal

class Dolphin(animal):

    def __init__(self,name,tricks):
        self.__name= name
        self.__tricks=tricks
    
    def __str__(self):
        return f"This is '{self.__name}' a dolphin who can do some tricks like {self.__tricks}"

    def doTricks(self):
        logging.info("Doing a random trick")
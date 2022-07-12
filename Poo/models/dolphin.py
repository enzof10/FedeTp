import logging
import webbrowser
from models.animal import animal

class Dolphin(animal):

    def __init__(self,name,tricks):
        self.__name= name
        self.__tricks=tricks
    
    def __str__(self):
        return f"This is '{self.__name}' a dolphin who can do some tricks like {self.__tricks}"


    @staticmethod
    def doTricks(self):
        return webbrowser.open_new("https://www.youtube.com/watch?v=OaJdsVCyhrI&ab_channel=JeremyLieurance")
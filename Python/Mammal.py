# -*- coding: UTF-8 -*-
from Animal import Animal
from Organism import Organism

class Mammal(Animal):
    def setNumberMammaryGlands(self, aNumberMammaryGlands):
        self.__numberMammaryGlands = aNumberMammaryGlands
    def getNumberMammaryGlands(self):
        return self.__numberMammaryGlands
    def grow(self):
        pass
    def eat (self):
        pass
    def giveBirth(self):
        pass
    
    def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex, aNumberMammaryGlands):
        Animal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex)
        self.setNumberMammaryGlands(aNumberMammaryGlands)
    def to_string(self):
        return "Number of Mammary Glands: "+str(self.getNumberMammaryGlands())
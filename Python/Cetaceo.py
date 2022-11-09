from Mammal import Mammal
from MarineAnimal import MarineAnimal

class Cetaceo(Mammal, MarineAnimal):
    def setType(self, aType):
        self.___type = aType
    def getType(self):
        return self.___type
    def grow(self):
        return "\nCetaceo growing"
    def eat (self):
        return "\nCetaceo eating"
    def giveBirth(self):
        return "\nCetaceo giving birth"
    def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex, numOfFins, aType, aNumberMammaryGlands):
        Mammal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex, aNumberMammaryGlands)
        MarineAnimal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex, numOfFins)
        self.___type = aType
        """@AttributeType String"""
    def to_string(self):
        return "Cetaceo=[\nType: "+self.getType() + " " +MarineAnimal.to_string(self)+ " " +Mammal.to_string(self)+"]"+self.grow()+self.eat()+self.giveBirth()  +"]"
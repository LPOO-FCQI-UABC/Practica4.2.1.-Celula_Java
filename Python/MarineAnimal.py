from Animal import Animal
from Organism import Organism
class MarineAnimal(Animal):
    def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex,numOfFins):
        Animal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex)
        self.___numOfFins = numOfFins
        """@AttributeType int"""
    def getNumOfFins(self):
        """@ReturnType int"""
        return self.___numOfFins
    def setNumOfFins(self, aNumOfFins):
        """@ParamType aNumOfFins int
        @ReturnType void"""
        self.___numOfFins = aNumOfFins
    def grow (self):
        pass
    def eat (self):
        pass
    def to_string(self):
        return "MarineAnimal=[\nNumOfFins: "+str(self.getNumOfFins())+ " " +Animal.to_string(self)+"]"
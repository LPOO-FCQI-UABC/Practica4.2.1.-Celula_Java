from Plant import Plant

class Tree(Plant):
    def setLeafType(self, aleafType):
        self.___leafType = aleafType
    def getLeafType(self):
        return self.___leafType
    def grow(self):
        return "Tree growing"
    def photosynthesis(self):
        return "Tree photosynthesis"
    def __init__(self, aName,aColor,aSize,aCell,aClassification,aleafType):
        Plant.__init__(self,aName,aColor,aSize,aCell,aClassification)
        self.___leafType = aleafType
        """@AttributeType String"""
    def to_string(self):
        return "Tree=[\nLeafType: "+self.getLeafType() + " " +Plant.to_string(self)+self.grow()+self.photosynthesis()+"]"
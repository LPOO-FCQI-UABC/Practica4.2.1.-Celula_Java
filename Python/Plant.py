from Organism import Organism

class Plant(Organism):
	def getClassification(self):
		"""@ReturnType String"""
		return self.___classification

	def setClassification(self, aClassification):
		"""@ParamType aClassification String
		@ReturnType void"""
		self.___classification = aClassification
	def grow (self):
		pass

	def photosynthesis(self):
		pass
	def __init__(self, aName,aColor,aSize,aCell,aClassification):
		Organism.__init__(self,aName, aColor, aSize, aCell)
		self.___classification = aClassification
		"""@AttributeType String"""
	def to_string(self):
		return "Plant=[\nClassification: "+self.___classification + " " + Organism.to_string(self)+"]"


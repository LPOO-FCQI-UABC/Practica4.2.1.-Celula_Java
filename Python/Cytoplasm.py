

class Cytoplasm(object):
	def getName(self):
		"""@ReturnType String"""
		return self.___name

	def setName(self, aName):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = aName

	def getProteinPercentage(self):
		"""@ReturnType int"""
		return self.___proteinPercentage

	def setProteinPercentage(self, aProteinPercentage):
		"""@ParamType aProteinPercentage int
		@ReturnType void"""
		self.___proteinPercentage = aProteinPercentage
  
	def getLipidsPercentage(self):
		"""@ReturnType int"""
		return self.___proteinPercentage

	def setLipidsPercentage(self, aLipidsPercentage):
		"""@ParamType aProteinPercentage int
		@ReturnType void"""
		self.___proteinPercentage = aLipidsPercentage

	def __init__(self, aName, aProteinPercentage, aLipidsPercentage):
		self.___name = aName
		"""@AttributeType String"""
		self.___proteinPercentage = aProteinPercentage
		"""@AttributeType int"""
		self.___lipidsPercentage = aLipidsPercentage
		"""@AttributeType int"""
		"""@AttributeType Cell
		# @AssociationType Cell
		# @AssociationMultiplicity 1"""
  
	def to_string(self):
		return "Cytoplasm=[\nName: "+self.___name+",\nProteinPercentage: "+str(self.___proteinPercentage)+",\nLipidsPercentage: "+str(self.___lipidsPercentage)+"]"

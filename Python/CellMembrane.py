import Cell

class CellMembrane(object):
	def getProteinPercentage(self):
		"""@ReturnType int"""
		return self.___proteinPercentage

	def setProteinPercentage(self, aProteinPercentage):
		"""@ParamType aProteinPercentage int
		@ReturnType void"""
		self.___proteinPercentage = aProteinPercentage

	def getLipidPercentage(self):
		"""@ReturnType int"""
		return self.___lipidPercentage

	def setLipidPercentage(self, aLipidPercentage):
		"""@ParamType aLipidPercentage int
		@ReturnType void"""
		self.___lipidPercentage = aLipidPercentage

	def getName(self):
		"""@ReturnType String"""
		return self.___name

	def setName(self, aName):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = aName

	def __init__(self, aName, aProteinPercentage, aLipidPercentage):
		self.___name = aName
		self.___proteinPercentage = aProteinPercentage
		self.___lipidPercentage = aLipidPercentage
		"""@AttributeType String"""
		"""@AttributeType int"""
		"""@AttributeType int"""
	def to_string(self):
		return "CellMembrane=[\nName: "+self.___name + " \nProteinPercentage: " + str(self.___proteinPercentage) + " \nLipidPercentage: " + str(self.___lipidPercentage)+"]"


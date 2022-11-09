
import Cell

class HereditaryMaterial(object):
	def getName(self):
		"""@ReturnType String"""
		return self.___name

	def setName(self, aName):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = aName

	def __init__(self, aName):
		self.___name = aName
		"""@AttributeType String"""
	def to_string(self):
		return "HereditaryMaterial=[\nName: "+self.___name+"]"


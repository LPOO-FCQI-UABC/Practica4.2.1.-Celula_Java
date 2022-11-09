
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Organism import Organism
from Cell import Cell

class Animal(Organism):
	def getSpecies(self):
		"""@ReturnType String"""
		return self.___species
	def setSpecies(self, aSpecies):
		"""@ParamType aSpecies String
		@ReturnType void"""
		self.___species = aSpecies
	def getSex(self):
		"""@ReturnType String"""
		return self.___theSex
	def setSex(self, aSex):
		"""@ParamType aSex String
		@ReturnType void"""
		self.___theSex = aSex
	def grow(self):
		pass
	def eat(self):
		pass
	def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex):
		Organism.__init__(self,aName, aColor, aSize, aCell)
		self.___species = aSpecies
		self.___theSex= aSex
		"""@AttributeType String"""
		"""@AttributeType String"""
	def to_string(self):
		return "Animal=[\nSpecies: "+self.___species+",\nSex: "+self.___theSex+ " " + Organism.to_string(self)+"]"
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HereditaryMaterial
import Cytoplasm
import Organism
import CellMembrane

class Cell(object):
	def getName(self):
		"""@ReturnType String"""
		return self.___name

	def setName(self, aName):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = aName

	def get_cytoplasm(self):
		"""@ReturnType String"""
		return self.___cytoplasm

	def set_cytoplasm(self, a_cytoplasm):
		self.___cytoplasm = a_cytoplasm

	def get_hereditary(self):
		"""@ReturnType String"""
		return self.___hereditary

	def set_hereditary(self, a_hereditary):
		"""@ParamType aName String
		@ReturnType void"""
		self.___hereditary = a_hereditary

	def get_cell_membrane(self):
		"""@ReturnType String"""
		return self.___cell_membrane

	def set_cell_membrane(self, a_cell_membrane):
		"""@ParamType aName String
		@ReturnType void"""
		self.___cell_membrane = a_cell_membrane

	def __init__(self, aName, aHereditary, aCytoplasm, aCellMembrane):
		self.___name = aName
		self.___hereditary = aHereditary
		self.___cytoplasm = aCytoplasm
		self.___cell_membrane = aCellMembrane
		"""@AttributeType String"""
		"""@AttributeType HereditaryMaterial
		# @AssociationType HereditaryMaterial"""
		"""@AttributeType Cytoplasm
		# @AssociationType Cytoplasm"""
		"""@AttributeType CellMembrane
		# @AssociationType CellMembrane"""
	def to_string(self):
		return "\nCELL=[Name: "+self.___name + " " + self.___hereditary.to_string() + " " + self.___cytoplasm.to_string() + " " + self.___cell_membrane.to_string()+"]"




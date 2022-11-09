#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Cell

class Organism(object):
    def setName(self, aName):
        """@ParamType aName String
        @ReturnType void"""
        self.___name = aName
    def getName(self):
        """@ReturnType String"""
        return self.___name
    def setCell(self, aCell):
        """@ParamType aCell Cell
        @ReturnType void"""
        self.___cell = aCell
    def getCell(self):
        """@ReturnType Cell"""
        return self.___cell
    def setColor(self, aColor):
        """@ParamType aColor String
        @ReturnType void"""
        self.___color = aColor
    def getColor(self):
        """@ReturnType String"""
        return self.___color
    def setSize(self, aSize):
        """@ParamType aSize int
        @ReturnType void"""
        self.___size = aSize
    def getSize(self):
        """@ReturnType int"""
        return self.___size
    def grow (self):
        pass

    def __init__(self, aName,aColor,aSize,aCell):
        self.___name = aName
        self.___cell = aCell
        self.___color = aColor
        self.___size = aSize
        """@AttributeType String"""
        """@AttributeType Cell
        # @AssociationType Cell
        # @AssociationMultiplicity 1"""
        """@AttributeType String"""
    def to_string(self):
        return "Organism=[\nName: "+self.___name+",\nColor: "+self.___color+",\nSize: "+str(self.___size)+",\nCell:"+self.___cell.to_string()+"]"

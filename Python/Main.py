from Cell import Cell
from Cetaceo import Cetaceo
from Organism import Organism
from Animal import Animal
from HereditaryMaterial import HereditaryMaterial
from Cytoplasm import Cytoplasm
from CellMembrane import CellMembrane
from Tree import Tree

class Main(object):
    newCell1=Cell("Cell1",HereditaryMaterial("HereditaryMaterial1"),Cytoplasm("Cytoplasm1",30,70),CellMembrane("CellMembrane1",10,90))
    newCell2=Cell("Cell2",HereditaryMaterial("HereditaryMaterial2"),Cytoplasm("Cytoplasm2",40,60),CellMembrane("CellMembrane2",20,80))
    newCell3=Cell("Cell3",HereditaryMaterial("HereditaryMaterial3"),Cytoplasm("Cytoplasm3",50,50),CellMembrane("CellMembrane3",30,70))
    newCell4=Cell("Cell4",HereditaryMaterial("HereditaryMaterial4"),Cytoplasm("Cytoplasm4",60,40),CellMembrane("CellMembrane4",40,60))

    newTree=Tree("Tree1","Green",100,newCell1,"Willow Tree","Leaf Type")
    print(newTree.to_string())

    newCataceo=Cetaceo("Dolphin","Blue",5,newCell1,"Marine Animal","Masculine",2,"Cataceo",2)
    print(newCataceo.to_string())
    
import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        System.out.println("////// ANIMAL ///////\n");
        Cell cell1 = new Cell("Cell 1", new Cytoplasms("Cytoplasm", 50, 50), new CellMembranes("Membrane", 4, 15), new HereditaryMaterial("Hereditary"));
        Cell cell2 = new Cell("Cell 2", new Cytoplasms("Cytoplasm", 15, 35), new CellMembranes("Membrane", 6, 1), new HereditaryMaterial("Hereditary"));
        
        ArrayList<Cell> vectorCells_Animals = new ArrayList<Cell>();
        vectorCells_Animals.add(cell1);
        vectorCells_Animals.add(cell2);
        Cetaceo animal = new Cetaceo(vectorCells_Animals, "Elephant", "Mammal","Blue", 4, "Feminine", 2);
        animal.to_String();


        System.out.println("\n/////// PLANTS ///////\n");
        Cell cell3 = new Cell("Cell 3", new Cytoplasms("Cytoplasm", 0, 100), new CellMembranes("Membrane", 66, 69), new HereditaryMaterial("Hereditary"));
        Cell cell4 = new Cell("Cell 4", new Cytoplasms("Cytoplasm", 89, 17), new CellMembranes("Membrane", 17, 05), new HereditaryMaterial("Hereditary"));
        Cell cell5 = new Cell("Cell 5", new Cytoplasms("Cytoplasm", 61, 79), new CellMembranes("Membrane", 81, 14), new HereditaryMaterial("Hereditary"));
        
        
        ArrayList<Cell> vectorCells_Plant = new ArrayList<Cell>();
        vectorCells_Plant.add(cell3);
        vectorCells_Plant.add(cell4);
        vectorCells_Plant.add(cell5);
        Tree plant = new Tree(vectorCells_Plant, "Tree", "Plant", "Green");
        plant.setTypeLeaf("Leaf");
        plant.to_String();
        
    }

    
}
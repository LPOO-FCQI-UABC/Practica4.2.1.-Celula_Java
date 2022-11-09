import java.util.ArrayList;

public class Tree extends Plant{

    private String typeLeaf;

    public Tree(ArrayList<Cell> vectorCells_Plant, String name, String classification, String color) {
        super(vectorCells_Plant, name, classification, color);
    }

    public void setTypeLeaf(String typeLeaf) {
        this.typeLeaf = typeLeaf;
    }
    public String getTypeLeaf() {
        return typeLeaf;
    }

    public void to_String(){
        System.out.println("Name: " + getName());
        System.out.println("Color: " + getColor());
        System.out.println("Classification: " + getClassification());
        System.out.println("Type of leaf: " + typeLeaf);
        System.out.println(grow());
        System.out.println(phtotossintesis());
        System.out.println("\nCELLS: ");
        for(Cell cell: getCells()){
            cell.to_String();
        }     
    }
 


}

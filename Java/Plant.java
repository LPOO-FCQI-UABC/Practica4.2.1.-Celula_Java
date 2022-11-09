import java.util.ArrayList;

public class Plant implements Organism{
    private String classification;
    private String name;
    private String color;
    private ArrayList<Cell> vectorCells_Plant;
	
	public Plant(ArrayList<Cell> vectorCells_Plant, String name, String classification, String color) {
        this.name = name;
        this.color = color;
        this.vectorCells_Plant = vectorCells_Plant;
        this.classification = classification;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public String getColor() {
        return color;
    }
    public void setCells(ArrayList<Cell> cells) {
        this.vectorCells_Plant = cells;
    }
    public ArrayList<Cell> getCells() {
        return vectorCells_Plant;
    }
    public void setClassification(String classification) {
        this.classification = classification;
    }
    public String getClassification() {
        return classification;
    }

    public void to_String(){
        System.out.println("Name: " + name);
        System.out.println("Color: " + color);
        System.out.println("Classification: " + classification);
        System.out.println("\nCELLS: ");
        for(Cell cell: vectorCells_Plant){
            cell.to_String();
        }     
    }

    public String grow() {
        String s = "The plant is growing";
        return s;
    }

    public String phtotossintesis() {
        String s = "The plant is doing phtotossintesis";
        return s;
    }
    
}
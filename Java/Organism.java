import java.util.ArrayList;

public abstract interface Organism {
    
    public abstract String getName();
    public abstract void setName(String name);
    public abstract String getColor();
    public abstract void setColor(String color);
    public abstract ArrayList<Cell> getCells();
    public abstract void setCells(ArrayList<Cell> cells);
    public abstract String grow(); /////////////


}

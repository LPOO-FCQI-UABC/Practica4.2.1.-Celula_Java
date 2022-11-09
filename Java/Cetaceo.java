import java.util.ArrayList;

public class Cetaceo implements Mammal, MarineAnimal{
    private ArrayList<Cell> cell1;
    private String name;
    private String species;
    private String sex;
    private String color;
    private int numberofFins;

    private int numberMammaryGlands;

    public Cetaceo(ArrayList<Cell> vectorCells_Animals, String name, String species, String color, int numberofFins, String sex, int numberMammaryGlands) {
        this.name = name;
        this.species = species;  
        this.cell1 = vectorCells_Animals;
        this.sex = sex;
        this.color = color;
        this.numberofFins = numberofFins;
        this.numberMammaryGlands = numberMammaryGlands;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
    public void setSpecies(String species) {
        this.species = species;
    }
    public String getSpecies() {
        return species;
    }
    
    public void to_String() {

        System.out.println("Name: " + name);
        System.out.println("Color: " + color);
        System.out.println("Specie: " + species);
        System.out.println("Sex: " + sex);
        System.out.println("Number of Mammary Glands: " + numberMammaryGlands);
        System.out.println(giveBirth());
        System.out.println(grow());
        System.out.println(eat());
        System.out.println("\nCELLS: ");
        for(Cell cell: cell1){
            cell.to_String();
        }
    }

    @Override
    public String getSex() {
        // TODO Auto-generated method stub
        return sex;
    }

    @Override
    public void setSex(String sex) {
        this.sex = sex;
    }

    @Override
    public String getColor() {
        // TODO Auto-generated method stub
        return color;
    }

    @Override
    public void setColor(String color) {
        // TODO Auto-generated method stub
        this.color = color;
    }

    @Override
    public ArrayList<Cell> getCells() {
        // TODO Auto-generated method stub
        return cell1;
    }

    @Override
    public void setCells(ArrayList<Cell> cells) {
        // TODO Auto-generated method stub
        this.cell1 = cells;
    }

    @Override
    public int getNumberofFins() {
        // TODO Auto-generated method stub
        return numberofFins;
    }

    @Override
    public void setNumberofFins(int numberofFins) {
        // TODO Auto-generated method stub
        this.numberofFins = numberofFins;
    }


    @Override
    public String grow() {
        String s = "The cetaceo is growing";
        return s;
    }

    public String eat() {
        String s = "The cetaceo is eating";
        return s;
    }

    public int getNumberMammaryGlands(){
        return numberMammaryGlands;
    }

    public void setNumberMammaryGlands(String numberMammaryGlands){
        this.numberMammaryGlands = numberMammaryGlands;
    }

    public void giveBirth(){
        String s = "El mamífero da a luz a su bebé expulsando una placenta a través de su utero";
        return s;
    }


    
}

public class CellMembranes {

	private String name;
    private int proteinPorcentage;
    private int lipidPorcentage;

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

    public CellMembranes(String n, int pP, int lP){
        name = n;
        proteinPorcentage = pP;
        lipidPorcentage = lP;
    }

    public void setLipid(int lP) {
		lipidPorcentage = lP;
	}
    public int getLipid() {
        return lipidPorcentage;
    }
    public void setProtein(int pP) {
		lipidPorcentage = pP;
	}
    public int getProtein() {
        return proteinPorcentage;
    }

    public void to_String(){
        System.out.println("\nType:" + name);
        System.out.println("Protein Porcentage: " + proteinPorcentage + "%");
        System.out.println("Lipid Porcentage: " +  lipidPorcentage+ "%");
    }
    
    
    

}
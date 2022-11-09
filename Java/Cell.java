public class Cell {

	Plant theLivingBeing;
	Animal theHumanBody;
	private  CellMembranes theCellMembrane;
	private  Cytoplasms theCytoplasm;
	private  HereditaryMaterial theHereditaryMaterial;
	private String name;
	

	public Cell(String name, Cytoplasms cytoplasm, CellMembranes cellMembranes, HereditaryMaterial hereditaryMaterial) {
		this.name = name;
		theCellMembrane = cellMembranes;
		theCytoplasm = cytoplasm;
		theHereditaryMaterial = hereditaryMaterial;
	}

    public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Cytoplasms getCytoplasms(){
		return theCytoplasm;
	}
	public void setCytoplasms(Cytoplasms c){
		theCytoplasm = c;
	}

	public CellMembranes getCellMembranes(){
		return theCellMembrane;
	}
	public void setCellMembranes(CellMembranes c){
		theCellMembrane = c;
	}

	public HereditaryMaterial getHereditaryMaterial(){
		return theHereditaryMaterial;
	}
	public void setHereditaryMaterial(HereditaryMaterial h){
		theHereditaryMaterial = h;
	}
	public void to_String(){
		System.out.println("Name: " + name);
		theCytoplasm.to_String();
		theCellMembrane.to_String();
		theHereditaryMaterial.to_String();  
    }
}

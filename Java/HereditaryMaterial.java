public class HereditaryMaterial {

	private String name;

	public HereditaryMaterial(String string) {
        name = string;
    }

    public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

    public void to_String(){
        System.out.println("\nCaracteristic:" + name);
    }

}
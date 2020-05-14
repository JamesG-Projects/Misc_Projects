package DAO;

import DAO.People;
import DAO.PeopleFactory;

public abstract class PrototypeColor implements Cloneable {
	public String name;
	public String state;
	public Integer zip;
	public String stateColor;
	
	public Object clone() 
    { 
        Object clone = null; 
        try 
        { 
            clone = super.clone(); 
        }  
        catch (CloneNotSupportedException e)  
        { 
            e.printStackTrace(); 
        } 
        return clone; 
    }
	
	public void getPerson() {
		System.out.println("");
		System.out.println("Name: " + name);
		System.out.println("State: " + state);
		System.out.println("Zip: " + zip);
		System.out.println("State Color: " + stateColor);
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setState(String state) {
		this.state = state;
	}
	
	public void setZip(Integer zip) {
		this.zip = zip;
	}
}

class Red extends PrototypeColor {
	public Red() {
		this.stateColor = "Red";
	}
}

class Blue extends PrototypeColor {
	public Blue() {
		this.stateColor = "Blue";
	}
}
package DAO;

import java.io.*;

public interface People {
	
	void setPerson(String name, String state, Integer zip);
	void getPerson();
	String getName();
	String getState();
	Integer getZip();
}

class validZipPerson implements People {
	String name;
	String state;
	int zip;
	
	public void setPerson(String pName, String pState, Integer pZip) {
		name = pName;
		state = pState;
		zip = pZip;
	}
	
	public void getPerson() {
		System.out.println("");
		System.out.println("Valid Zip Code");
		System.out.println("Name: " + name);
		System.out.println("State: " + state);
		System.out.println("Zip: " + zip);
	}
	
	public String getName() {
		return name;
	}
	public String getState() {
		return state;
	}
	public Integer getZip() {
		return zip;
	}
}

class invalidZipPerson implements People {
	String name;
	String state;
	int zip;
	
	public void setPerson(String pName, String pState, Integer pZip) {
		String name = pName;
		String state = pState;
		int zip = pZip;
	}
	
	public void getPerson() {
		System.out.println("");
		System.out.println("!!Invalid Zip Code!!");
		System.out.println("Name: " + name);
		System.out.println("State: " + state);
		System.out.println("Zip: " + zip);
	}
	
	public String getName() {
		return name;
	}
	public String getState() {
		return state;
	}
	public Integer getZip() {
		return zip;
	}
	
}
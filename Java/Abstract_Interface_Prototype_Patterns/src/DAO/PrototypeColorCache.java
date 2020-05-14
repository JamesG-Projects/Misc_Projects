package DAO;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import DAO.PrototypeColor;


public class PrototypeColorCache {
	public static Map<String, PrototypeColor> colorMap = new HashMap<String, PrototypeColor>();
	public static Map<String, String> stateColorDic = new HashMap<String, String>();
	
	public static PrototypeColorCache instance = new PrototypeColorCache();

	public static PrototypeColorCache getInstance() {
		return instance;
	}
	
	public static void loadCache() {
		colorMap.put("Red", new Red()); colorMap.put("Blue", new Blue());
		stateColorDic.put("AL","RED"); stateColorDic.put("HI","BLUE"); stateColorDic.put("MA","BLUE"); stateColorDic.put("NM","BLUE"); stateColorDic.put("SD","RED");
		stateColorDic.put("AK","RED"); stateColorDic.put("ID","RED"); stateColorDic.put("MI","RED"); stateColorDic.put("NY","BLUE"); stateColorDic.put("TN","RED");
		stateColorDic.put("AZ","RED"); stateColorDic.put("IL","BLUE"); stateColorDic.put("MN","BLUE"); stateColorDic.put("NC","RED"); stateColorDic.put("TX","RED");
		stateColorDic.put("AR","RED"); stateColorDic.put("IN","RED"); stateColorDic.put("MS","RED"); stateColorDic.put("ND","RED"); stateColorDic.put("UT","RED");
		stateColorDic.put("CA","BLUE"); stateColorDic.put("IA","RED"); stateColorDic.put("MO","RED"); stateColorDic.put("OH","RED"); stateColorDic.put("VT","BLUE");
		stateColorDic.put("CO","BLUE"); stateColorDic.put("KS","RED"); stateColorDic.put("MT","RED"); stateColorDic.put("OK","RED"); stateColorDic.put("VA","BLUE");
		stateColorDic.put("CT","BLUE"); stateColorDic.put("KY","RED"); stateColorDic.put("NE","RED"); stateColorDic.put("OR","BLUE"); stateColorDic.put("WA","BLUE");
		stateColorDic.put("DE","BLUE"); stateColorDic.put("LA","RED"); stateColorDic.put("NV","BLUE"); stateColorDic.put("PA","RED"); stateColorDic.put("WV","RED");
		stateColorDic.put("FL","RED"); stateColorDic.put("ME","BLUE"); stateColorDic.put("NH","BLUE"); stateColorDic.put("RI","BLUE"); stateColorDic.put("WI","RED");
		stateColorDic.put("GA","RED"); stateColorDic.put("MD","BLUE"); stateColorDic.put("NJ","BLUE"); stateColorDic.put("SC","RED"); stateColorDic.put("WY","RED");
	}
	
	public PrototypeColor getPrototypeColor( People validZipPerson ) 
    { 
		String name = validZipPerson.getName();
		String state = validZipPerson.getState();
		int zip = validZipPerson.getZip();
		
		if (stateColorDic.get(validZipPerson.getState()) == "RED") {
			PrototypeColor Red = (PrototypeColor) colorMap.get("Red").clone();
			Red.setName(name); Red.setState(state); Red.setZip(zip);
			return Red;
		}
		else {
			PrototypeColor Blue = (PrototypeColor) colorMap.get("Blue").clone();
			Blue.setName(name); Blue.setState(state); Blue.setZip(zip);
			return Blue;
		}
    }
}

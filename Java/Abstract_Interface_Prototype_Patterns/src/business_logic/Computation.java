package business_logic;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import DAO.FileIO;

public class Computation {

	public int counter = 0;

	private Map<String, String> mapList;

	public Computation(String file) throws IOException {
		
		//Create first instance and print instance address
		FileIO f = FileIO.getInstance();
		mapList = f.getMap(file);
		//System.out.println(f);
		
		//Create second instance and print instance address
//		FileIO f2 = FileIO.getInstance();
//		mapList = f.getMap(file);
		//System.out.println(f2);
	}

	//print name and zip code
	public List<String> printAllNameAndZipCode() {
		Set set = mapList.entrySet();// Converting to Set so that we can traverse
		Iterator itr = set.iterator();
		List<String> printList = new ArrayList<String>();
		while (itr.hasNext()) {
			// Converting to Map.Entry so that we can get key and value separately
			Map.Entry entry = (Map.Entry) itr.next();
			String firstName = entry.getKey().toString().split(" ")[0].toString();
			String lastName = entry.getKey().toString().split(" ")[1].toString();
			String[] address = entry.getValue().toString().split(",");
			String zipCode = entry.getValue().toString().split(",")[address.length - 1];
			
			//zipCode = zipCode + "-1234";
			
			printList.add("First name: " + firstName);
			printList.add("Last name: " + lastName);
			printList.add("ZIP Code: " + zipCode);
			
			//String newZipCode = zipCode + "-1234";
			//zipCode = zipCode + "-1234";
			//String newAddress = String.format("address: %s,%s,%s,%s", address[0], address[1], address[2], zipCode);
//			System.out.println(newAddress);
		}
		return printList;
	}
}

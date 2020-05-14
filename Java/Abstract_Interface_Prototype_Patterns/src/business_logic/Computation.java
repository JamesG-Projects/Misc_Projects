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
		FileIO f = FileIO.getInstance();
		mapList = f.getMap(file);
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
			printList.add("First name: " + firstName);
			printList.add("Last name: " + lastName);
			printList.add("ZIP Code: " + zipCode);
		}
		return printList;
	}
}

package business_logic;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Selection{



	public static List<String> SelectionBlueStateList= Arrays.asList("WA","CA","VA","VT","RI","OR","NY","NM","NJ","NH","NV","MN","MA","MD","ME","IL","HI","DC","DE","CT","CO","CA");
	public static List<String> SelectionRedStateList=Arrays.asList("PA","ND","SD","NE","KS","IA","MO","WI","IN","MI","OH","TX","OK","AR","LA","MS","AL","TN","KY","GA","FL","SC","NC","WV","ID","UT","AZ","MT","WY","AK");
	public static List<String> SelectionBlueGroup = new ArrayList<String>();
	public static List<String> SelectionRedGroup = new ArrayList<String>();
	public Selection() throws IOException{
	}
	@SuppressWarnings("rawtypes")
	public void SelectionPhaser(String selection) throws CloneNotSupportedException, IOException {
		DistinguishZipCodeFactory DZ=new DistinguishZipCodeFactory();
		Phaser validList=DZ.GetPhaser("valid");
		ValidZipCode valList_copy=((ValidZipCode) validList).clone();
		Map<Integer, String> tempMap= valList_copy.ZipCodePhaser();
		Set set = tempMap.entrySet();// Converting to Set so that we can traverse
		Iterator itr = set.iterator();
		try {
			while (itr.hasNext()) {
				Map.Entry entry = (Map.Entry) itr.next();
				String[] address = entry.getValue().toString().split(",");
				String stCode = entry.getValue().toString().split(",")[address.length - 3].trim();
				switch(selection) {
				case "Blue":
					if(SelectionBlueStateList.contains(stCode)) {
						SelectionBlueGroup.add(entry.getValue().toString() + "Selection State: Blue");
					}
					break;
				case "Red":
					if(SelectionRedStateList.contains(stCode)) {
						SelectionRedGroup.add(entry.getValue().toString() + "Selection State: Red");
					}
					break;
				}
			}
		}catch(Exception e) {
			Map.Entry entry = (Map.Entry) itr.next();
			System.out.println(" ERROR input : " + entry.getValue()+ "not match correct form");
		}
	}
	public List<String> SelectionBluePhaser() throws CloneNotSupportedException, IOException {
		SelectionPhaser("Blue");
		return SelectionBlueGroup;
	}

	public int GetSelectionBlueGroupSize() {
		return SelectionBlueGroup.size();
	}

	public List<String> SelectionRedPhaser() throws CloneNotSupportedException, IOException {
		SelectionPhaser("Red");
		return SelectionRedGroup;
	}
	public int GetSelectionRedGroupSize() {
		return SelectionRedGroup.size();
	}
	public void InfoPrinter(List<String> l) {
		for(String a:l) {
			System.out.println(a);
		}
	}
}

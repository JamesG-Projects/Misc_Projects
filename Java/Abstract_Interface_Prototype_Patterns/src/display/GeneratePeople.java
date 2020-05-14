package display;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import Singleton.Singleton;
import DAO.PeopleFactory;
import DAO.People;
import DAO.PrototypeColorCache;

class GeneratePeople {

	public static void main(String[] args) throws IOException {
		
		Map<String, ArrayList<Integer>> zipDictionary;
		List<People> validZipPersonList = new ArrayList<People>();

		//Feature 1
		Singleton feature1 = new Singleton();
		
		//Feature 2
		PeopleFactory feature2 = PeopleFactory.getInstance();
		zipDictionary = feature2.getZipDictionary("Java\\Abstract_Interface_Prototype_Patterns\\zipCode_info.xlsx");
		feature2.getPerson("Java\\Abstract_Interface_Prototype_Patterns\\input_sample2.txt", zipDictionary, validZipPersonList);
		
		//Feature 3
		PrototypeColorCache.loadCache();
		PrototypeColorCache feature3 = PrototypeColorCache.getInstance();
		for(int i = 0; i < validZipPersonList.size(); i++) {
			feature3.getPrototypeColor(validZipPersonList.get(i)).getPerson();
		}
	}
}


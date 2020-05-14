package display;

import java.io.IOException;
import business_logic.Computation;
import Singleton.Singleton;

public class FileDisplay {

	public static void main(String[] args) throws IOException {

		Singleton feature1 = new Singleton();
		Computation file1 = new Computation("input_sample2.txt");
		
		for (String a : file1.printAllNameAndZipCode()) {
			System.out.println(a);
		}
	}
}

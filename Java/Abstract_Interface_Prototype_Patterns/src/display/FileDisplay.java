package display;

import java.io.IOException;
import business_logic.Computation;

public class FileDisplay {

	public static void main(String[] args) throws IOException {

		Computation file1 = new Computation("Jan27-Jan31-input-sample.txt");
		for (String a : file1.printAllNameAndZipCode()) {
			System.out.println(a);
		}
	}
}

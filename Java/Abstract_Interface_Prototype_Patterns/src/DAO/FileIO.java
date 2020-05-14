package DAO;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FileIO {

	private static Map<String, String> map = new HashMap<String, String>();

//Task2 : Solution-A ( line16-line 24)
	private static FileIO instance = new FileIO();

	public FileIO() {

	}

	public static FileIO getInstance() {
		return instance;
	}

//Task2 : Solution-B (line 27-line36)
//	private static FileIO instance;
//
//	public FileIO() {
//	}
//	public static FileIO getInstance() {
//		if(instance==null) {
//			instance=new FileIO();
//		}
//		return instance;
//	}

	
	// read .txt file, read data and save data in map
	private static void readFile(String file) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(file));
		String st;
		List<String> tempList = new ArrayList<String>();
		while ((st = br.readLine()) != null) {
			tempList.add(st.trim().toString());
		}
		for (int i = 0; i < tempList.size(); i++) {
			if (tempList.get(i).toString().contains("name:")) {
				map.put(tempList.get(i).trim().substring(6).toString(), tempList.get(i + 1).substring(9).toString());
			}
		}
		br.close();
	}

	// return map information
	public Map<String, String> getMap(String file) throws IOException {
		readFile(file);
		return map;
	}
}

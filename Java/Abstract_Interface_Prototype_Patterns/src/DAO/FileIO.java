package DAO;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.*;

import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class FileIO {

	private static Map<String, String> map = new HashMap<String, String>();

	
//Task2 : Solution-A ( line16-line 24)
	private static FileIO instance = new FileIO();

	//private constructor
	private FileIO() {
		//constructor-related initializations
	}

	//public, global access point to access the instance
	public static FileIO getInstance() {
		return instance;
	}

//Task2 : Solution-B (line 27-line36)
//	private static FileIO instance;
//	
//	//private constructor
//	private FileIO() {
//		//constructor-related initializations
//	}
//	
//	//public, global point to access the instance
//	public static FileIO getInstance() {
//		if(instance==null) {
//			instance=new FileIO();
//		}
//		return instance;
//	}

	//=================================================================================================================
	//ORIGINAL
	//=================================================================================================================
	// read .txt file, read data and save data in map
//	private static void readFile(String file) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader(file));
//		
//		String st;
//		List<String> tempList = new ArrayList<String>();
//		while ((st = br.readLine()) != null) {
//			tempList.add(st.trim().toString());
//		}
// 		for (int i = 0; i < tempList.size(); i++) {
//			if (tempList.get(i).toString().contains("name:")) {
//				map.put(tempList.get(i).trim().substring(6).toString(), tempList.get(i + 1).substring(9).toString());
//			}
//		}
//		br.close();
//	}
	
	
	//=================================================================================================================
	//FIND ZIP REGEX  =================================================================================================
	//=================================================================================================================
	@SuppressWarnings("deprecation")
	private static void readFile(String file) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(file));
		String st;
		List<String> tempList = new ArrayList<String>();
		
																													   //Regex setup for finding ZIP code
		String regex = "\\d{5}$"; 																					   //Finds all occurrences of digits in groups of 5 at the ends of lines
		Pattern zipPattern = Pattern.compile(regex);
		Matcher zipMatcher;
		
		String tempStr; 																							   //Temporary string to store edited address
		while ((st = br.readLine()) != null) {
			
																													   //Find a valid zipcode, add "-1234" to the end of the string, store in tempList
			zipMatcher = zipPattern.matcher(st.trim().toString());
			if(zipMatcher.find()) {
//				tempStr = st.trim().toString() + "-1234";
				tempStr = st.trim().toString();
				tempList.add(tempStr);
			}
																													   //If a zipcode can't be found, don't edit and just store the string in tempList
			else {
				tempList.add(st.trim().toString());
			}
		}
		
																													   //Initialize a BufferedWriter instance for writing back to the text file
		BufferedWriter bw = new BufferedWriter(new FileWriter(file));
		
 		for (int i = 0; i < tempList.size(); i++) {
			if (tempList.get(i).toString().contains("name:")) {
				map.put(tempList.get(i).trim().substring(6).toString(), tempList.get(i + 1).substring(9).toString());
			}
																													   //Try to write back to the original file
			try { 																									   //Iterate through tempList, overwrite the original file
				bw.write(tempList.get(i).toString());
				if(i < tempList.size()-1) {
					bw.write("\n");
				}
			} catch (IOException e) { 																				   //Catch & print any errors
	            e.printStackTrace();
			}
		}
		br.close();
		bw.close();
		
	//=================================================================================================================
	//START XLSX READER ===============================================================================================
	//=================================================================================================================
		Map <String, ArrayList<Integer>> zipDictionary = new HashMap<String, ArrayList<Integer>>();
		
		try { 
			File xlFile = new File("Java\\Abstract_Interface_Prototype_Patterns\\zipCode_info.xlsx"); 	   //creating a new file instance
			FileInputStream fis = new FileInputStream(xlFile); 														   //obtaining bytes from the file
			XSSFWorkbook wb = new XSSFWorkbook(fis); 																   //creating Workbook instance that refers to .xlsx file
			XSSFSheet sheet = wb.getSheetAt(0); 																	   //creating a Sheet object to retrieve object
			Iterator<Row> itr = sheet.iterator();																	   //iterating over excel file
			
			while (itr.hasNext()) {
				Row row = itr.next();
				Iterator<Cell> cellIterator = row.cellIterator(); 													   //iterating over each column
				
				String state; 																						   //Create "state" variable to store state abbreviations from xlsx file
				int minZip, maxZip; 																				   //Create min and max zip variables to store Zip Min and Zip Max values from xlsx file
				
				while (cellIterator.hasNext()) {
					Cell cell = cellIterator.next();
					switch (cell.getCellType()) {
					
					case Cell.CELL_TYPE_STRING: 																	   //field that represents string cell type
//						System.out.print(cell.getStringCellValue() + "\t\t\t");
						
						//COMMENTING OUT THIS "IF" STATEMENT ALLOWS FOR SUCCESSFUL PRINTING OF XLSX FILE
						if(cell.getStringCellValue().length() == 2) { 												   //Find the state abbreviations
							Cell cell2 = cellIterator.next();
																													   //Logic to confirm we have a state abbreviation followed by two integer cells "zip min" and "zip max"
							if(cell2.getCellType() == Cell.CELL_TYPE_NUMERIC || cell2.getStringCellValue().length() == 5) {
								state = cell.getStringCellValue(); 													   //Store the state abbreviation
								ArrayList<Integer> zipMinMax= new ArrayList<Integer>(); 							   //Create an array list to store minZip and maxZip
								
								switch (cell2.getCellType()) {
								
								case Cell.CELL_TYPE_STRING:
									
																													   //Sometimes Zip Min and Zip Max from xlsx file are strings rather than ints
									minZip = Integer.parseInt(cell2.getStringCellValue());							   //Parse the strings to ints
									cell2 = cellIterator.next();										               //Go to next cell
									maxZip = Integer.parseInt(cell2.getStringCellValue());							   //Parse the strings to ints
//									System.out.println(state + " " + minZip + " " + maxZip);
									
									zipMinMax.add(minZip);
									zipMinMax.add(maxZip);
									zipDictionary.put(state, zipMinMax);
									
//									System.out.println("zipMinMax: " + zipMinMax);
//									System.out.println("");
//									System.out.println("zipDictionary: " + zipDictionary);
									break;
									
								case Cell.CELL_TYPE_NUMERIC:
									minZip = (int)cell2.getNumericCellValue();
									cell2 = cellIterator.next();
									maxZip = (int)cell2.getNumericCellValue();
//									System.out.println(state + " " + minZip + " " + maxZip);
									
									zipMinMax.add(minZip);
									zipMinMax.add(maxZip);
									zipDictionary.put(state, zipMinMax);
									
//									System.out.println("zipMinMax: " + zipMinMax);
//									System.out.println("");
//									System.out.println("zipDictionary: " + zipDictionary);
									break;
								}
							}
						}
						
						break;
					
					case Cell.CELL_TYPE_NUMERIC: 																	   //field that represents number cell type
//						System.out.print(cell.getNumericCellValue() + "\t\t\t");
						break;
					}
				}
//				System.out.println("");
			}
			System.out.println("zipDictionary: " + zipDictionary);
			wb.close();
		}  
		catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	//=================================================================================================================
	
	// return map information
	public Map<String, String> getMap(String file) throws IOException {
		readFile(file);
		return map;
	}
}

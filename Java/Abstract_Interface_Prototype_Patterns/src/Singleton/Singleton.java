package Singleton;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Singleton {
	
	public Singleton() throws IOException {
		
	//=================================================================================================================
	//START XLSX READER ==== FEATURE1 =================================================================================
	//=================================================================================================================
		System.out.println("=================================================================================================================");
		System.out.println("= START XLSX READER ==== FEATURE 1 ==============================================================================");
		System.out.println("=================================================================================================================");
		
		try { 
			File xlFile = new File("Java\\Abstract_Interface_Prototype_Patterns\\zipCode_info.xlsx"); //creating a new file instance
			FileInputStream fis = new FileInputStream(xlFile); //obtaining bytes from the file
			XSSFWorkbook wb = new XSSFWorkbook(fis); //creating Workbook instance that refers to .xlsx file
			XSSFSheet sheet = wb.getSheetAt(0); //creating a Sheet object to retrieve object
			Iterator<Row> itr = sheet.iterator(); //iterating over excel file
			
			while (itr.hasNext()) {
				Row row = itr.next();
				Iterator<Cell> cellIterator = row.cellIterator(); //iterating over each column
				
				while (cellIterator.hasNext()) {
					Cell cell = cellIterator.next();
					switch (cell.getCellType()) {
					
					case Cell.CELL_TYPE_STRING: //field that represents string cell type
						System.out.print(cell.getStringCellValue() + "\t\t\t");
						break;
					
					case Cell.CELL_TYPE_NUMERIC: //field that represents number cell type
						System.out.print(cell.getNumericCellValue() + "\t\t\t");
						break;
					
					default:
						break;
					}
				}
				System.out.println("");
			}
		}  
		catch(Exception e) {
			e.printStackTrace();
		}
		System.out.println("=================================================================================================================");
		System.out.println("= END FEATURE 1 =================================================================================================");
		System.out.println("=================================================================================================================");
		System.out.println("");
	}

}

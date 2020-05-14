package DAO;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class FileIO {

	public static Map<Integer, String> InputPeopleInfo = new HashMap<Integer, String>();
	public static Map<String, String> InputZipCodeRangeInfo = new HashMap<String, String>();
	public static int PersonUniqueID=0;
	public static FileIO instance = new FileIO();
	public static String ZipCodeInfo_InputPath="";
	public static String PersonalAddress_InputPath="";

	private FileIO() {

	}

	public static FileIO getInstance() {
		return instance;
	}

	//read .Txt file
	public static void ReadTxt() throws IOException {
		String path=PersonalAddress_InputPath;
		try {
			BufferedReader br = new BufferedReader(new FileReader(path));

			String st;
			List<String> tempList = new ArrayList<String>();
			while ((st = br.readLine()) != null) {
				tempList.add(st.trim().toString());
			}
			for (int i = 0; i < tempList.size(); i++) {
				if (tempList.get(i).toString().contains("name:")) {
					String tempAddress=tempList.get(i).trim()+","+tempList.get(i+1).trim();		
					InputPeopleInfo.put(PersonUniqueID, tempAddress);
					PersonUniqueID++;				
				}
			}
			br.close();
		}catch(Exception e){
			e.printStackTrace();
			System.out.println("Input file fail or can;t read, check FileIO class");
		}
	}

	//read Excel file
	public static void ReadExcelSheet() throws IOException {

		try  
		{  
			String path2=ZipCodeInfo_InputPath;
			File f1 = new File(path2);   //creating a new file instance  
			FileInputStream fis = new FileInputStream(f1);   //obtaining bytes from the file  
			XSSFWorkbook wb = new XSSFWorkbook(fis);   
			XSSFSheet sheet = wb.getSheetAt(0);     //creating a Sheet object to retrieve object  
			for(int rowIndex=1;rowIndex<= sheet.getLastRowNum();rowIndex++) {
				XSSFRow row =sheet.getRow(rowIndex);
				if(row!=null) {
					Cell cellStFullName=row.getCell(1);
					Cell cellSt=row.getCell(2);
					Cell cellMin = row.getCell(3);
					Cell cellMax = row.getCell(4);
					String temp=null;		
					try {
						temp=(int)cellMin.getNumericCellValue()+"_"+(int)cellMax.getNumericCellValue()+"_"+cellStFullName.getStringCellValue().toString();
					}catch(Exception e){
						temp=cellMin+"_"+cellMax+"_"+cellStFullName.getStringCellValue().toString();
					}
					InputZipCodeRangeInfo.put(cellSt.toString(),temp);
				}
			}
			wb.close();
		}  
		catch(Exception e)  
		{  
			e.printStackTrace(); 
			System.out.println("Input file fail or can;t read, check FileIO class");

		}  	
	}

	//return Map for official zip code range info
	public Map<String, String> GetOfficialZipcodeRangeInfo() throws IOException {
		if(InputZipCodeRangeInfo.size()==0) {
			ReadExcelSheet();
		}
		return InputZipCodeRangeInfo;
	}

	//return Map for personal information
	public Map<Integer, String> GetPeopleInfo() throws IOException {
		if(InputPeopleInfo.size()==0) {
			ReadTxt();
		}		
		return InputPeopleInfo;
	}
}

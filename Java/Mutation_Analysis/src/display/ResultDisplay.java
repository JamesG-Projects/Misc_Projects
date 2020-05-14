package display;

import java.io.IOException;

import DAO.FileIO;
import business_logic.DistinguishZipCodeFactory;
import business_logic.District;
import business_logic.Selection;
import business_logic.Phaser;

public class ResultDisplay {

	public static void main(String[] args) throws IOException, CloneNotSupportedException {

		//input path
		FileIO.ZipCodeInfo_InputPath="zipCode_info.xlsx";
		FileIO.PersonalAddress_InputPath="input_sample3.txt";

		//Phaser for valid and invalid group
		DistinguishZipCodeFactory DZ=new DistinguishZipCodeFactory();
		Phaser valid=DZ.GetPhaser("valid");
		valid.GetSize();
		//valid.InfoPrinter();   //print detail for valid group
		Phaser invalid=DZ.GetPhaser("invalid");	
		invalid.GetSize();
		//invalid.InfoPrinter();   //print detail for invalid group

		//Phaser for Selection		
		System.out.println("-----Selection-----");
		Selection selection =new Selection();
		selection.SelectionBluePhaser();
		System.out.println("Blue selection group= "+selection.GetSelectionBlueGroupSize());
		selection.SelectionRedPhaser();
		System.out.println("Red selection group= "+ selection.GetSelectionRedGroupSize());
		System.out.println("Total valid people at 2 Selection Group: "+(selection.GetSelectionBlueGroupSize()+selection.GetSelectionRedGroupSize()));
		System.out.println("-----end-----");


		//Phaser for Region
		System.out.println("-----Region-----");
		District district=new District();
		district.Region_NortheastPhaser();
		//district.InfoPrinter(district.Region_NortheastPhaser());
		System.out.println("Northeast group= "+district.GetNortheastGroupSize());	
		district.Region_MidwestPhaser();
		System.out.println("Midwest group= "+ district.GetMidwestGroupSize());
		district.Region_SouthPhaser();
		System.out.println("South group= "+ district.GetSouthGroupSize());
		district.Region_WestPhaser();
		System.out.println("West group= " + district.GetWestGroupSize());
		System.out.println("Total valid people at 4 region: "+ (district.GetNortheastGroupSize()+district.GetMidwestGroupSize()+district.GetSouthGroupSize()+district.GetWestGroupSize()));
		System.out.println("-----end-----");


		//Phaser for District information		
		System.out.println("-----Name and District information-----");
		district.DistrictPhaser("District");
		for(String i:District.AllDistrictResultList) {
			System.out.println(i);
		}
		System.out.println("-----District Summary-----");
		System.out.println(District.DistrictSummary);
		System.out.println("-----end-----");
	}

}

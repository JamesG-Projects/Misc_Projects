package business_logic;

import java.io.IOException;
import java.util.Map;

public interface Phaser extends Cloneable {

	Map<Integer, String> ZipCodePhaser() throws IOException;
	int GetSize();
	public void InfoPrinter();
}

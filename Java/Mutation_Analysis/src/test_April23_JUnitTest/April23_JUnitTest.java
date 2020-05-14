package test_April23_JUnitTest;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class April23_JUnitTest {

	@Test
	void testValidZipCodeMutation1() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode>tempMin && currentCode<=tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation2() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode<tempMin && currentCode<=tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation3() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode<=tempMin && currentCode<=tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation4() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode<tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation5() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode>tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation6() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode>=tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	@Test
	void testValidZipCodeMutation7() {
        String stCode = "FL";
        int tempMin = 32004;
        int tempMax = 34997;
        int currentCode = 33133;

        if(stCode != null) {
            if((currentCode>=tempMin || currentCode<=tempMax)) {
            	assertTrue(true);
            }
            fail("Mutant Killed");
        }
    }
	
	
	
	@Test
	void testInvalidZipCodeMutation1() {
        String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode>tempMin && currentCode<=tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation2() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode<tempMin && currentCode<=tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation3() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode<=tempMin && currentCode<=tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation4() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode<tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation5() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode>tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation6() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode>=tempMin && currentCode>=tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
	@Test
	void testInvalidZipCodeMutation7() {
		String stCode = "OH";
        int tempMin = 43001;
        int tempMax = 45999;
        int currentCode = 99231;

        if(stCode != null) {
            if((currentCode>=tempMin || currentCode<=tempMax)) {
                fail("Mutant Killed");
            }
            assertTrue(true);
        }
    }
	
}

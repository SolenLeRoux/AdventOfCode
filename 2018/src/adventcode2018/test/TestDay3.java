package adventcode2018.test;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import adventcode2018.Day3;

class TestDay3 extends TestDay {

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		solver = new Day3();
	}

	@Test
	void testSolvePart1_1() {
		// Custom test case
		int part = 1;
		String[] testCase = {
				"#1 @ 1,3: 4x4",
				"#2 @ 3,1: 4x4", 
				"#3 @ 5,5: 2x2"
				};
		String expected = "4";
		
		// Solve the problem
		runTest(part, testCase, expected);
	}

	@Test
	void testSolvePart2_1() {
		// Custom test case
		int part = 2;
		String[] testCase = {
				"#1 @ 1,3: 4x4",
				"#2 @ 3,1: 4x4", 
				"#3 @ 5,5: 2x2"
				};
		String expected = "3";

		// Solve the problem
		runTest(part, testCase, expected);
	}

}

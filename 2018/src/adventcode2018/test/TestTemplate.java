package adventcode2018.test;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import adventcode2018.Template;

class TestTemplate extends TestDay {

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		solver = new Template();
	}

	@Test
	void testSolvePart1_1() {
		// Custom test case
		int part = 1;
		String[] testCase = {};
		String expected = "nothing";
		
		// Solve the problem
		runTest(part, testCase, expected);
	}

	@Test
	void testSolvePart2_1() {
		// Custom test case
		int part = 2;
		String[] testCase = {};
		String expected = "nothing";

		// Solve the problem
		runTest(part, testCase, expected);
	}

}

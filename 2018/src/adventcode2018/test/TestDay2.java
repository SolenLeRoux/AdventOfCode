package adventcode2018.test;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import adventcode2018.Day2;

class TestDay2 extends TestDay {

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		solver = new Day2();
	}

	@Test
	void testSolvePart1_1() {
		// Custom test case
		int part = 1;
		String[] testCase = {"abcdef"};
		String expected = "0";
		
		// Solve the problem
		runTest(part, testCase, expected);
	}

	@Test
	void testSolvePart1_2() {
		// Custom test case
		int part = 1;
		String[] testCase = {"bababc", "abbcde"};
		String expected = "2";

		// Solve the problem
		runTest(part, testCase, expected);
	}

	@Test
	void testSolvePart1_3() {
		// Custom test case
		int part = 1;
		String[] testCase = {"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"};
		String expected = "12";

		// Solve the problem
		runTest(part, testCase, expected);
	}

	@Test
	void testSolvePart2_1() {
		// Custom test case
		int part = 2;
		String[] testCase = {"abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"};
		String expected = "fgij";

		// Solve the problem
		runTest(part, testCase, expected);
	}

}

package adventcode2018.test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

import adventcode2018.Day2;
import adventcode2018.Solution;

class TestDay2 {
	
	Solution solver = new Day2();
	
	void test(int part, String[] testCase, String expected) {
		List<String> input = new ArrayList<String>(Arrays.asList(testCase));
		String result = solver.solve(part, input);
		System.out.println("Got " + result + ", expected " + expected);
		assertTrue(expected.equals(result));
	}

	@Test
	void testSolvePart1_1() {
		// Custom test case
		int part = 1;
		String[] testCase = {"abcdef"};
		String expected = "0";
		
		// Solve the problem
		test(part, testCase, expected);
	}

	@Test
	void testSolvePart1_2() {
		// Custom test case
		int part = 1;
		String[] testCase = {"bababc", "abbcde"};
		String expected = "2";

		// Solve the problem
		test(part, testCase, expected);
	}

	@Test
	void testSolvePart1_3() {
		// Custom test case
		int part = 1;
		String[] testCase = {"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"};
		String expected = "12";

		// Solve the problem
		test(part, testCase, expected);
	}

	@Test
	void testSolvePart2_1() {
		// Custom test case
		int part = 2;
		String[] testCase = {"abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"};
		String expected = "fgij";

		// Solve the problem
		test(part, testCase, expected);
	}

}

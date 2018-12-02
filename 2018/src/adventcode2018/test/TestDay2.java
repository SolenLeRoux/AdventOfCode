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

	@Test
	void testSolvePart1_1() {
		// Custom test case
		String[] testCase = {"abcdef"};
		String expected = "0";
		
		// Solve the problem
		List<String> input = new ArrayList<String>(Arrays.asList(testCase));
		String result = solver.solvePart1(input);
		System.out.println("Got " + result + ", expected " + expected);
		assertTrue(expected.equals(result));
	}

	@Test
	void testSolvePart1_2() {
		// Custom test case
		String[] testCase = {"bababc", "abbcde"};
		String expected = "2";
		
		// Solve the problem
		List<String> input = new ArrayList<String>(Arrays.asList(testCase));
		String result = solver.solvePart1(input);
		System.out.println("Got " + result + ", expected " + expected);
		assertTrue(expected.equals(result));
	}

	@Test
	void testSolvePart1_3() {
		// Custom test case
		String[] testCase = {"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"};
		String expected = "12";
		
		// Solve the problem
		List<String> input = new ArrayList<String>(Arrays.asList(testCase));
		String result = solver.solvePart1(input);
		System.out.println("Got " + result + ", expected " + expected);
		assertTrue(expected.equals(result));
	}

	@Test
	void testSolvePart2() {
		// fail("Not yet implemented");
	}

}

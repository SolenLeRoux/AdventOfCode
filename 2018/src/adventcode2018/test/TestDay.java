package adventcode2018.test;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import adventcode2018.Solution;

public abstract class TestDay {
	
	public static Solution solver;

	public void runTest(int part, String[] testCase, String expected) {
		List<String> input = new ArrayList<String>(Arrays.asList(testCase));
		String result = solver.solve(part, input);
		System.out.println("Got " + result + ", expected " + expected);
		assertTrue(expected.equals(result));
	}

}

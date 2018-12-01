package adventcode2018;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public abstract class Solution {
	
	public static List<String> getInput(int day) throws IOException {
		/**
		 * Returns the input as a list of lines
		 * @params the day of the challenge, an int from 1 to 25
		 * @returns a list containing each line of the input
		 * @throws IOException if there was any problem reading the file
		 */
		
		// Read the file
		String fileName = "inputs/input" + day + ".txt";
		BufferedReader txt = new BufferedReader(new FileReader(fileName));
		String line;
		
		// Fill the list line by line
		List<String> input = new ArrayList<String>();
		while ((line = txt.readLine()) != null) {
		    input.add(line);
		};
		
		// Close file and return the input
		txt.close();
		return input;
	}
	
	public String solve(int part, List<String> input) {
		/**
		 * Solves the right problem with the right input
		 * @params the problem we want to solve (either 1 or 2) and the input
		 * @returns the solution as a String
		 * @throws IllegalArgumentException if the part requested isn't 1 or 2
		 */
		if (part == 1) {
			return solvePart1(input);
		} else if (part == 2) {
			return solvePart2(input);
		} else {
			throw new IllegalArgumentException("Invalid part: " + part);
		}
	}
	
	public abstract String solvePart1(List<String> input);
	
	public abstract String solvePart2(List<String> input);
	
}
import java.util.Dictionary;
import java.util.Hashtable;
import java.util.List;

public class Day1 extends Solution {
	
	public String solvePart1(List<String> input) {
		/**
		 * solves the problem 1 of day 1
		 * @param a list of int written as Strings, with their sign as first char
		 * for instance: {"+12", "-300"}
		 * @return the sum of each line
		 * for instance: 300 - 12 = 288
		 */
		int sum = 0;
		for (String line : input) {
			sum += decodeLine(line);
		}
		return Integer.toString(sum);
	};
	
	private int decodeLine(String line) {
		/**
		 * decodes a line of the input
		 * @param an int written as a String, with its sign as first char
		 * for instance: "+12" or "-300"
		 * @return the int that matches the input
		 * for instance: 12 or -300
		 * @throws IllegalArgumentException if the string does not start with either + or -
		 */
		char symbol = line.charAt(0);
		int value = Integer.parseInt(line.substring(1));
		if (symbol == '+') {
			return value;
		} else if (symbol == '-') {
			return -value;
		} else {
			throw new IllegalArgumentException("Lines must start with + or -, not " + symbol);
		}
	}
	
	public String solvePart2(List<String> input) {
		/**
		 * solves the problem 2 of day 1
		 * @param a list of int written as Strings, with their sign as first char
		 * for instance: {"+12", "-300"}
		 * @return the first time a sum is reached twice when adding the values of each line
		 * in an infinite loop
		 */
		Dictionary<Integer, Integer> frequencies = new Hashtable<Integer, Integer>();
		boolean found = false;
		int i = 0;
		int freq = 0;
		String line;
		while (!found) {
			line = input.get(i % input.size());
			freq += decodeLine(line);
			if (frequencies.get(freq) != null) {
				frequencies.put(freq,  2);
				found = true;
			} else {
				frequencies.put(freq,  1);
			}
			i++;
		}
		return Integer.toString(freq);
	};

}
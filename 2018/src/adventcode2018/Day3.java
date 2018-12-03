package adventcode2018;

import java.util.Dictionary;
import java.util.Hashtable;
import java.util.List;

public class Day3 extends Solution {
	
	private int[] parseLine(String line) {
		/**
		 * parse a line of the input into usable data
		 * @param a String of the form "#{code} @ {left},{top}: {width}x{height}"
		 * @return an array of int of the form {code, left, top, width, height}
		 */
		String[] parsed = line.split("[ #@,x:]+");
		int code = Integer.parseInt(parsed[1]);
		int left = Integer.parseInt(parsed[2]);
		int top = Integer.parseInt(parsed[3]);
		int width = Integer.parseInt(parsed[4]);
		int height = Integer.parseInt(parsed[5]);
		return new int[] {code, left, top, width, height};
	}
	
	public String solvePart1(List<String> input) {
		/**
		 * we have a fabric which is a large matrix (of more than 1000 inches each side)
		 * and a list of claims to use a portion of this fabriq. This method returns the
		 * number of square inches of this fabriq that are claimed more than once
		 * @param a list of claims of the form "#{code} @ {left},{top}: {width}x{height}"
		 * @return the number of square inches claimed more than once
		 */
		Dictionary<String, Integer> fabric = new Hashtable<String, Integer>();
		int count = 0;
		for (String line: input) {
			int[] parsed = parseLine(line);
			int left = parsed[1], top = parsed[2], width = parsed[3], height = parsed[4];
			for (int i = left; i < left + width; i++) {
				for (int j = top; j < top + height; j++) {
					int n = fabric.get(i + "," + j) != null ? fabric.get(i + "," + j) + 1 : 1;
					fabric.put(i + "," + j, n);
					if (n == 2) count++;
				}
			}
		}
		return Integer.toString(count);
	};
	
	public String solvePart2(List<String> input) {
		/**
		 * we have a fabric which is a large matrix (of more than 1000 inches each side)
		 * and a list of claims to use a portion of this fabriq. This method returns the
		 * first claim that does not collide with any other
		 * @param a list of claims of the form "#{code} @ {left},{top}: {width}x{height}"
		 * @return the code of the first claim that does not collide with any other
		 */
		Dictionary<String, Integer> fabric = new Hashtable<String, Integer>();
		Dictionary<Integer, Boolean> codes = new Hashtable<Integer, Boolean>();
		for (String line: input) {
			int[] parsed = parseLine(line);
			int code = parsed[0], left = parsed[1], top = parsed[2], width = parsed[3],
					height = parsed[4];
			boolean valid = true;
			for (int i = left; i < left + width; i++) {
				for (int j = top; j < top + height; j++) {
					if (fabric.get(i + "," + j) == null) {
						fabric.put(i + "," + j, code);
					} else {
						valid = false;
						int otherCode = fabric.get(i + "," + j);
						codes.put(otherCode, false);
					}
				}
			}
			codes.put(code,  valid);
		}
		for (String line: input) {
			int[] parsed = parseLine(line);
			int code = parsed[0];
			if (codes.get(code)) return Integer.toString(code);
		}
		return "not found";
	};

}
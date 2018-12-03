package adventcode2018;

import java.util.Dictionary;
import java.util.Hashtable;
import java.util.List;

public class Day3 extends Solution {
	
	public String solvePart1(List<String> input) {
		Dictionary<String, Integer> fabric = new Hashtable<String, Integer>();
		int count = 0;
		for (String line: input) {
			String[] parsed = line.split("[ #@,x:]+");
			int left = Integer.parseInt(parsed[2]);
			int top = Integer.parseInt(parsed[3]);
			int width = Integer.parseInt(parsed[4]);
			int height = Integer.parseInt(parsed[5]);
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
		return "nothing";
	};

}
package adventcode2018;
import java.io.IOException;
import java.util.Dictionary;
import java.util.Hashtable;

public class Main {
	
	private static Dictionary<String, String> decodeArguments(String[] args) {
		/**
		 * transforms user input into usable data
		 * @param user input as a list of Strings
		 * @return a dict matching useful params to their value
		 * TODO: support '-all'
		 */
		Dictionary<String, String> params = new Hashtable<String, String>();
		for (int i = 0; i < args.length - 1; i++) {
			if ("-d".equals(args[i])) {
				params.put("day", args[i+1]);
			}
			if ("-p".equals(args[i])) {
				params.put("part", args[i+1]);
			}
			if ("-t".equals(args[i])) {
				params.put("test", args[i+1]);
			}
		}
		return params;
	}
	
	private static Solution getSolution(int day) {
		/**
		 * gets the right Solution object depending on the day asked
		 * @param the day requested
		 * @return a Solution object matching the day requested
		 * @throws IllegalArgumentException if the day requested is not found
		 */
		if (day == 1) {
			return new Day1();
		} else if (day == 2) {
			return new Day2();
		} else if (day == 3) {
			return new Day3();
		} else if (day == 4) {
			return new Day4();
		} else {
			throw new IllegalArgumentException("Day " + day + " is not available (yet)");
		}
	}

	public static void main(String[] args) {
		// get user input
		Dictionary<String, String> params = decodeArguments(args);
		
		// find out day and part
		int day = Integer.parseInt(params.get("day"));
		int part = Integer.parseInt(params.get("part"));
		
		// get solution requested
		Solution solution = getSolution(day);
		try {
			System.out.println(solution.solve(part, Solution.getInput(day)));
		} catch (IOException e) {
			System.out.println("There was a problem while trying to load the input");
			e.printStackTrace();
		}
	}

}

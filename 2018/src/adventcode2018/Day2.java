package adventcode2018;
import java.util.Dictionary;
import java.util.Hashtable;
import java.util.List;

public class Day2 extends Solution {
	
	public String solvePart1(List<String> input) {
		/**
		 * get the checksum of a list of codes
		 * @param a list of codes which are random strings like "efmghuxckqldtwjzvitbparnno"
		 * @return the number of codes which have the same char exactly twice
		 * times the number of codes which have the same char exactly thrice
		 */
		int two = 0;
		int three = 0;
		Dictionary<Character, Integer> occurences;
		for (String word : input) {
			occurences = new Hashtable<Character, Integer>();
			int thisTwo = 0;
			int thisThree = 0;
			for (int i = 0; i < word.length(); i++) {
				char letter = word.charAt(i);
				int occurence = occurences.get(letter) != null ? occurences.get(letter) + 1 : 1;
				occurences.put(letter, occurence);
				if (occurence == 2) {thisTwo++;}
				if (occurence == 3) {thisTwo--; thisThree++;}
				if (occurence == 4) {thisThree--;}
			}
			if (thisTwo > 0) two++;
			if (thisThree > 0) three++;
		}
		return Integer.toString(two * three);
	};
	
	public String solvePart2(List<String> input) {
		/**
		 * Find the first two words with exactly one letter different
		 * @input a list of words
		 * @return the common letters between the two matching words
		 */
		String wordA, wordB, same;
		int diff;
		for (int i = 0; i < input.size() - 1; i++) {
			for (int j = i + 1; j < input.size(); j++) {
				wordA = input.get(i);
				wordB = input.get(j);
				same = "";
				diff = 0;
				for (int l = 0; l < wordA.length(); l++) {
					if (wordA.charAt(l) != wordB.charAt(l)) {diff++;}
					else {same += wordA.charAt(l);}
					if (diff > 1) {break;}
				}
				if (diff == 1) {return same;}
			}
		}
		return "not found";
	};

}
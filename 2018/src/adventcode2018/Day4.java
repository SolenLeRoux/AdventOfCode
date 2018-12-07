package adventcode2018;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.Hashtable;
import java.util.List;

public class Day4 extends Solution {
	
	public void parseInput(List<String> input, Map<String, Shift> shifts, Map<Integer, Guard> guards) {
		/**
		 * parse the whole input given by this problem to fill the two map given
		 * as inputs
		 * @input a list of String that look like "YYYY-MM-DD HH:MM something happened",
		 * and two dictionaries of {date : shift} and {id : guard} that we need to complete
		 * @return nothing, but we completed the two maps
		 */
		for (String line: input) {
			// Get time informations
			String date = line.substring(1, 11);
			int hour = Integer.parseInt(line.substring(12, 14));
			int minute = Integer.parseInt(line.substring(15, 17));
			
			// If hour starts at 23h, we need to consider next day
			if (hour != 0) {
				int day = Integer.parseInt(line.substring(9, 11));
				date = date.substring(0, 8) + String.format("%02d", day + 1);
			}
			
			// Get or create corresponding shift
			Shift shift = shifts.get(date);
			if (shift == null) {
				shift = new Shift(date);
				shifts.put(date, shift);
			}
			
			// Find out if its a starts shift / falls asleep / wakes up situation
			String situation = line.substring(19);
			if (situation.substring(0, 5).equals("Guard")) {
				// If it's a starts shift situation, get the guard's ID
				// and update or start corresponding shift
				int id = Integer.parseInt(situation.split("[# ]")[2]);
				Guard guard = guards.get(id);
				if (guard == null) {
					guard = new Guard(id);
					guards.put(id, guard);
				}
				shift.setGuard(guard);
				guard.addShift(shift);
			}
			else if (situation.equals("falls asleep")) {
				shift.addSleep(minute);
			}
			else if (situation.equals("wakes up")) {
				shift.addWake(minute);
			}
		}
	}
	
	public String solvePart1(List<String> input) {
		/**
		 * We want to find out from logs when the guards will most probably be asleep
		 * To do this, we need to find out which guard sleeps the most and when he sleeps
		 * @input a list of String that look like "YYYY-MM-DD HH:MM something happened"
		 * @return the id of the guard chosen time the minute when they will be asleep
		 */
		
		// parse input
		Map<String, Shift> shifts = new Hashtable<String, Shift>();
		Map<Integer, Guard> guards = new Hashtable<Integer, Guard>();
		
		parseInput(input, shifts, guards);
		
		// find out which guard has slept the most
		Guard guardMostAsleep = null;
		int minutesSlept = 0;
		for (int guardID: guards.keySet()) {
			Guard guard = guards.get(guardID);
			if (guard.getTimeAsleep() > minutesSlept) {
				guardMostAsleep = guard;
				minutesSlept = guardMostAsleep.getTimeAsleep();
			}
		}
		
		// find out when this guard was the most asleep
		int[] minutesWhenAsleep = guardMostAsleep.getMinuteWhenSlept();
		int max = 0;
		int bestMinute = 0;
		for (int minute = 0; minute < 60; minute++) {
			if (minutesWhenAsleep[minute] > max) {
				max = minutesWhenAsleep[minute];
				bestMinute = minute;
			}
		}
		
		// return ID of guard most asleep * minute when most asleep
		return Integer.toString(guardMostAsleep.id * bestMinute);
	};
	
	public String solvePart2(List<String> input) {
		/**
		 * We want to find out from logs when the guards will most probably be asleep
		 * To do this, we will proceed the other way : find out which minute has a
		 * guard that is often asleep, and then which guard it is
		 * @input a list of String that look like "YYYY-MM-DD HH:MM something happened"
		 * @return the id of the guard chosen time the minute when they will be asleep
		 */
		
		// parse input
		Map<String, Shift> shifts = new Hashtable<String, Shift>();
		Map<Integer, Guard> guards = new Hashtable<Integer, Guard>();
		
		parseInput(input, shifts, guards);
		
		// find out which minute was the most slept by a guard,
		// and which guard it is
		int max = 0;
		int bestMinute = 0;
		Guard bestGuard = null;
		for (int guardID: guards.keySet()) {
			Guard guard = guards.get(guardID);
			int[] asleep = guard.getMinuteWhenSlept();
			for (int minute = 0; minute < 60; minute++) {
				if (asleep[minute] > max) {
					max = asleep[minute];
					bestMinute = minute;
					bestGuard = guard;
				}
			}
		}
		
		// return guard id * minute chosen
		return Integer.toString(bestGuard.id * bestMinute);
	};

}

class Shift {
	
	String date;
	Guard guard;
	List<Integer> fallsAsleep = new ArrayList<Integer>();
	List<Integer> wakesUp = new ArrayList<Integer>();
	private boolean sorted = false;
	
	public Shift(String date) {
		this.date = date;
	}
	
	public void setGuard(Guard guard) {
		this.guard = guard;
	}
	
	public void addSleep(int minute) {
		fallsAsleep.add(minute);
	}
	
	public void addWake(int minute) {
		wakesUp.add(minute);
	}
	
	private void sortLists() {
		if (!sorted) {
			Collections.sort(fallsAsleep);
			Collections.sort(wakesUp);
			sorted = true;
		}
	}
	
	public int[][] getSleepIntervals() {
		/**
		 * gets the interval when the guard is asleep during this shift
		 * @return a list of intervals [start, end[ when the guard is asleep
		 */
		sortLists();
		int[][] intervals = new int[fallsAsleep.size()][2];
		for (int i = 0; i < fallsAsleep.size(); i++) {
			int[] interval = { fallsAsleep.get(i), wakesUp.get(i) };
			intervals[i] = interval;
		}
		return intervals;
	}
	
	public int getMinutesAsleep() {
		/**
		 * gets the time the guard spent asleep during this shift
		 * @return the number of minutes the guard was asleep
		 */
		sortLists();
		int result = 0;
		for (int i = 0; i < fallsAsleep.size(); i++) {
			result += wakesUp.get(i) - fallsAsleep.get(i);
		}
		return result;
	}
	
}

class Guard {
	
	int id;
	List<Shift> shifts = new ArrayList<Shift>();
	
	public Guard(int id) {
		this.id = id;
	}
	
	public void addShift(Shift shift) {
		shifts.add(shift);
	}
	
	public List<Shift> getShifts() {
		return shifts;
	}
	
	public int getTimeAsleep() {
		/**
		 * @return the number of minutes this guard was asleep during all their shifts
		 */
		int result = 0;
		for (Shift shift: shifts) {
			result += shift.getMinutesAsleep();
		}
		return result;
	}
	
	public int[] getMinuteWhenSlept() {
		/**
		 * @return an array of 60 elements, that represent for each minute the number
		 * of time we found this guard asleep during this minute
		 */
		int[] timeAsleep = new int[60];
		for (Shift shift: shifts) {
			int[][] intervalsAsleep = shift.getSleepIntervals();
			for (int[] interval : intervalsAsleep) {
				for (int i = interval[0]; i < interval[1]; i++) {
					timeAsleep[i] += 1;
				}
			}
		}
		return timeAsleep;
	}
	
}
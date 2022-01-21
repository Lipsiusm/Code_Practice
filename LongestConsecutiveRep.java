/*For a given string s find the character c (or C) 
with longest consecutive repetition and return:

Object[]{c, l};

where l (or L) is the length of the repetition. 
If there are two or more characters with the same l 
return the first in order of appearance.

For empty string return:

Object[]{"", 0}*/


import java.util.*;

public class LongestConsecutiveRep{
	public static void main (String [] args){
		System.out.println("Enter a string Gamer: ");
		Scanner input = new Scanner(System.in);
		String input_string=input.nextLine();
		Object [] values = longestRepetition(input_string);

		for (int k = 0; k < values.length ; k++){
			System.out.println(values[k]);
		}
	}

	    public static Object[] longestRepetition(String s) {
        
        String inputString = s;
        char compare_char = ' ';
        char temp_char = ' ';
        char max_char = ' ';
        int max_count= 0;
        int count = 1;

        //if the length is 0, return specified object
        if (inputString.length() == 0){
            return new Object [] {"", 0};
        }

        for (int i=0; i<inputString.length(); i++){

        	temp_char = inputString.charAt(i);
        	//making the assumption temp_char = compare_char
        	// if not we reset count & char

            if (temp_char != compare_char){
            	compare_char = temp_char;
            	count = 1;
            }
            //setting return values once we find the max
            if (max_count < count){
            	max_count = count;
            	max_char = compare_char;
            }
            //otherwise increment count
            count++;
        }
        //cast to the specified object (string)
        //return the object array
        String return_char = Character.toString(max_char);
        return new Object []{return_char, max_count};
    }
}

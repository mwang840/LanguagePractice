import java.util.Arrays;
import java.lang.Object;
public class CommonPrefix{
    public static String longestCommonPrefix(String[] strs) {
        //If the string length is zero return ""
        
        if(strs.length == 0 ){
            return "";
        }
        //If the size of the string is one
        //return the string
        else if(strs.length == 1){
            return strs[0];
        }
        //Else sort the string alphabetically
        Arrays.sort(strs);
        //Set the length of the int to the first length of the string
        int firstLength = strs[0].length();
        //Have a string to contain the prefix
        StringBuilder longestPrefix = new StringBuilder();
        //loop over the string array
        for(int i = 0; i < firstLength; i++){
            //
            if(strs[0].charAt(i) == strs[strs.length - 1].charAt(i)){
                longestPrefix.append(strs[0].charAt(i));
            }
            else{
                break;
            }
        }
        return longestPrefix.toString();
    }

    public static void main(String[] args) {
        String[] testOne = {"flower","flow","flight"};
        System.out.println(longestCommonPrefix(testOne));
        String[]testTwo = {"dog","racecar","car"};
        System.out.println(longestCommonPrefix(testTwo));
    }
}

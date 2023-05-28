import java.lang.StringBuilder;

public class AddingBigNumbers {
    public static String add(String a, String b) {
       //Check if a's length is greater than bs length and vice versa, then swap it with string b
       if(a.length() > b.length()){
        String temp = a;
        a = b;
        b = temp;
       }
       String result = "";
       int a_len = a.length(), b_len = b.length();

       //Reverse both Strings via string builder
       a = new StringBuilder(a).reverse().toString();
       b = new StringBuilder(b).reverse().toString();
       //Create carry over for digit overflow
       int digitOverflow = 0;
       for(int i = 0; i < a_len; i++){
            int totalSum = ((int)(a.charAt(i) - '0') + (int)(b.charAt(i) - '0') + digitOverflow);
            result += (char)(totalSum % 10 + '0');
            digitOverflow = totalSum / 10;
       }
       //Add remaining digits of the larger number
       for(int i = a_len; i < b_len; i++){
        int totalSum = ((int)(b.charAt(i) - '0') + digitOverflow);
        result += (char)(totalSum % 10 + '0');
        digitOverflow = totalSum / 10;
       }
       //Adds the remaining left overs
       if(digitOverflow > 0){
        result+= (char)(digitOverflow + '0');
       }
       result = new StringBuilder(result).reverse().toString().replaceFirst("^0+(?!$)", "");
       return result;
      }

    public static void main(String[] args) {
        System.out.println(add("1", "1"));
        System.out.println(add("123", "456"));
        System.out.println(add("888", "222"));
        System.out.println(add("63829983432984289347293874", "90938498237058927340892374089"));
    }  
}

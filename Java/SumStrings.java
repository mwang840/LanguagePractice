import java.lang.StringBuilder;
public class SumStrings{

    public static String sumStrings(String a, String b){
        //Idea
        int pointer1 = a.length()-1;
        int pointer2 = b.length()-1;
        int carry = 0;
       StringBuilder sumStr = new StringBuilder();
        while(pointer1 >=0 || pointer2 >=0 || carry >0){
            int digit1 = (pointer1>=0)? a.charAt(pointer1) - '0' : 0;
            int digit2 = (pointer2>=0)? b.charAt(pointer2) - '0': 0;
            int sumCol = digit1 + digit2 + carry;
            sumStr.append(Integer.toString(sumCol % 10));
            carry = sumCol /10;
            pointer1--;
            pointer2--;
        }
        
        return sumStr.reverse().toString().replaceFirst("^0+(?!$)", "");
    }

    public static void main(String[] args) {
        String example = "123";
        String example2 = "456";
        System.out.println(sumStrings(example, example2));
    }   
}
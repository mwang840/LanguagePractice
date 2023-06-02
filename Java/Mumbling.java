public class Mumbling {
    public static String accum(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            String lowerCasing = s.substring(i, i + 1).toLowerCase();
            String upperCasing = s.substring(i, i + 1).toUpperCase();
            result += upperCasing;
            for (int j = 1; j <= i; j++) {
                result += lowerCasing;
            }
            if (i != s.length() - 1) {
                result += "-";
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(accum("abcd"));
        System.out.println(accum("RqaEzty"));
        System.out.println(accum("cwAt"));
    }
}
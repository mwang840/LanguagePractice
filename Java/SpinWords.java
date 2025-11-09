public class SpinWords {
     
    
    public static String spinWords(String sentence) {
       
        String[] splitWords = sentence.split(" ");
        StringBuilder Sb = new StringBuilder();
        for(String word: splitWords){
            if(word.length() >= 5){
                Sb.append(new StringBuilder(word).reverse().toString());
            }
            else{
                Sb.append(word);
            }
            Sb.append(" ");
        }
        return Sb.toString().trim();
    }

    public static void main(String[] args) {
        String example = "University of Delaware";
        System.out.println(spinWords(example));
    }
}

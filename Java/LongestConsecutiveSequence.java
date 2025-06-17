import java.util.HashSet;
import java.util.Set;

class LongestConsecutiveSequence{
    public static int longestConsecutive(int[] nums) {
        //Try this in a hash
        Set<Integer> sortedArray = new HashSet<Integer>();
        int numConsecutive = 0;
        for (int num : nums){
            sortedArray.add(num);
        }

        for(int value : nums){
            if(sortedArray.contains(value) && !sortedArray.contains(value - 1)){
                int current = value, count = 0;
                while(sortedArray.contains(current)){
                    sortedArray.remove(current);
                    current++;
                    count++;
                }
                numConsecutive = Math.max(numConsecutive, count);
            }
        }
        return numConsecutive;
    }



    public static void main(String[] args) {
        int []example1 = {100,4,200,1,3,2};
        System.out.println(longestConsecutive(example1));
        
    }
}
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class TargetIndecies {
    public static List<Integer> targetIndices(int[] nums, int target) {
        int tracker = 0;
        int smallTracker = 0;
        List<Integer> targetVal = new ArrayList<Integer>();
        Arrays.sort(nums);
        // System.out.print(nums);
        for (int i = 0; i < nums.length; i++){
            if(nums[i] == target){
                tracker++;
            }
            if(nums[i] < target){
                smallTracker++;
            }
        }
        while (tracker > 0) {
            targetVal.add(smallTracker++);
            tracker--;
        }
        return targetVal;
    }

    public static void main(String[] args) {
        int[] number = {1, 2, 5, 2, 3};
        
        System.out.println(targetIndices(number, 5));
    }
}

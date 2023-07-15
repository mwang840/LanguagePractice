import java.util.HashMap;
import java.util.Map;

class TwoSum {
    public static int[] twoSum(int[] arr, int target) {
        // Initialize map with all possible sums from given pair
        // initialize temp sum and array with size two
        // check if temp sum hits the target
        // return the indicies of the array/map
        Map<Integer, Integer> values = new HashMap<Integer, Integer>();
        for (int i = 0; i < arr.length; i++) {
            int difference = target - arr[i];
            if (values.containsKey(difference)) {
                return new int[] { values.get(difference), i };
            } else {
                values.put(arr[i], i);
            }
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        int arr1[] = { 2, 7, 11, 15 };
        System.out.println(twoSum(arr1, 9).toString());
    }
}
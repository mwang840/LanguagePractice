public class BinarySearch {
    public static int search(int[] nums, int target) {
        int minimum = 0;
        int maximum = nums.length;
        while(minimum < maximum){
            int middle = (maximum + minimum) / 2;
            if(nums[middle] < target){
                minimum = middle + 1;
            }
            else if(nums[middle] > target){
                maximum = middle;
            }
            else{
                return middle;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr1[] = {5, 8, 3, 10, 15};
        System.out.print(search(arr1, 3));
    }
}

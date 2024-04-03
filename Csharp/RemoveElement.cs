public class RemoveElement {
    public int Remove(int[] nums, int val) {
        //Thought process
        //loop through array, check if the array position is NOT equal to the val
        //Add those to the new array
        //return the length of that array
        int point = 0;
        for(int i = 0; i < nums.Length; i++){
            if(nums[i] != val){
                nums[point] = nums[i];
                point++;
            }
        }
        return point;
    }

    public void Main(){
        int[] numsOne = {3, 2, 2, 3};
        int removeOne = Remove(numsOne, 3);
        Console.WriteLine("Removed one is", removeOne);
    }
}
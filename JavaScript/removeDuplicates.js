var removeDuplicates = function(nums) {
    if (nums.length === 0) {
        return 0;
    }

    // Use two pointers approach
    let slow = 0;

    for (let fast = 1; fast < nums.length; fast++) {
        if (nums[fast] !== nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }

    return slow + 1;
};

var main = function(){
    const input1 = [0,0,1,1,1,2,2,3,3,4];
    console.log(removeDuplicates(input1));
    const input2 = [1, 1, 2]
    console.log(removeDuplicates(input2));
}

main()
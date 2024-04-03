class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){};
    TreeNode(int val){
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class RangeSumBst {
    public static int rangeSumBST(TreeNode root, int low, int high) {
        TreeNode current = root;
        int rangeSum = 0;
        if(root == null){
            return 0;
        }
        if(root.val >= low && root.val <= high){
            rangeSum = current.val;
        }
        int leftSum = rangeSumBST(current.left, low, high);
        int rightSum = rangeSumBST(current.right, low, high);
        return rangeSum + leftSum + rightSum;
    }



    public static void main(String[] args) {
        TreeNode second = new TreeNode(5);
        TreeNode third = new TreeNode(15);
        TreeNode first = new TreeNode(10, second, third);
        TreeNode fourth = new TreeNode(3);
        TreeNode fifth = new TreeNode(7);
        TreeNode sixth = new TreeNode(18);
        TreeNode seventh = new TreeNode(1);
        TreeNode eight = new TreeNode(6);
        TreeNode ninth = new TreeNode(13);
        second.left = fourth;
        second.right = fifth;
        fourth.left = seventh;
        fifth.left = eight;
        third.left = ninth;
        third.right = sixth;
        System.out.println(rangeSumBST(first, 6, 10));
    }
}
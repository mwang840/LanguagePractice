class TreeNode {
 val: number
left: TreeNode | null
 right: TreeNode | null
 constructor(val: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function goodNodes(root: TreeNode): number {
   return treeTraversal(root, root.val);
};

function treeTraversal(root: TreeNode | null, value: number){
   if(root === null){
    return 0;
   }

   let goodNodeCount = (root.val >= value ? 1: 0);
   value = Math.max(root.val, value)
   return goodNodeCount + treeTraversal(root.left, value) + treeTraversal(root.right, value);
}
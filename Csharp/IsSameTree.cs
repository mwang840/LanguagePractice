using System;
using System.Reflection.Metadata.Ecma335;
using System.Text;
namespace SameTree
{
    internal class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
          this.val = val;
          this.left = left;
          this.right = right;
        }
         public bool IsSameTree(TreeNode p, TreeNode q){
            if(p == null && q == null){
                return true;
            }
            else{
                return (p.val == q.val && IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right));
            }
        }
    }

}
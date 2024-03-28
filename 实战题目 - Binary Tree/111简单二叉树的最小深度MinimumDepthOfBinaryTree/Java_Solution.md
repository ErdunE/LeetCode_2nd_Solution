```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {

        if(root == null){
            return 0;
        }

        //这道题递归条件里分为三种情况
        //1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if(root.left == null && root.right == null){
            return 1;
        }

        //2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度
        int leftNode = minDepth(root.left);
        int rightNode = minDepth(root.right);
        //这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1;
        if(root.left == null || root.right == null){
            return leftNode + rightNode + 1;
        }

        //3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
        return Math.min(leftNode, rightNode) + 1;
        
    }
}
```

时间复杂度：O(n) 递归过程中对每个节点都访问 1 次

空间复杂度：O(n) 用了额外的栈空间，栈的大小取决于二叉树的高度，二叉树最坏情况下的高度为 n



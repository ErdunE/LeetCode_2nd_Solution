
## 前序遍历
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
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    public boolean isValidBST(TreeNode node, long left, long right){
        // 判断空节点
        if(node == null){
            return true;
        }
        // 记录当前节点值
        long x = node.val;

        // 首先必须在区间范围内 即 left < x < right
        // 同时左子树必须是二叉搜索树 即 isValidBST(node.left, left, x)
        // 同时右子树必须是二叉搜索树 即 isValidBST(node.right, x, right)
        return left < x && right > x && isValidBST(node.left, left, x) && isValidBST(node.right, x, right);
    }
}
```
时间复杂度：O(n)，其中 n 为二叉搜索树的节点个数。   
空间复杂度：O(n)。最坏情况下，二叉搜索树退化成一条链，因此递归需要 O(n) 的栈空间。


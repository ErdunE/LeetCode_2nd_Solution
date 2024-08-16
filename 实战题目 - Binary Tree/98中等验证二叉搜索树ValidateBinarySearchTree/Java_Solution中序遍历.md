
## 中序遍历
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
    // 初始化pre结点的值
    private long pre = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        // 判断空节点/边界条件
        if(root == null){
            return true;
        }
        // 判断左边，如果不行或小于前结点值 返回false
        if(!isValidBST(root.left) || root.val <= pre){
            return false;
        }
        // pre值等于当前节点值
        pre = root.val;
        // 递归右子树
        return isValidBST(root.right);
    }
}
```
时间复杂度：O(n)，其中 n 为二叉搜索树的节点个数。   
空间复杂度：O(n)。最坏情况下，二叉搜索树退化成一条链，因此递归需要 O(n) 的栈空间。


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
    public List<Integer> inorderTraversal(TreeNode root) {
        // 中序遍历：左 - 中 - 右
        List<Integer> res = new ArrayList<Integer>();
        dfs(res, root);
        return res;
    }

    void dfs(List<Integer> res, TreeNode root){
        if(root == null){
            return;
        }

        // 按照 左-中-右的方式遍历
        dfs(res, root.left);
        res.add(root.val);
        dfs(res, root.right);
    }
}
```
终止条件：当前节点为空时    
函数内：递归的调用左节点，打印当前节点，再递归调用右节点

时间复杂度：O(n)    
空间复杂度：O(h)，h是树的高度



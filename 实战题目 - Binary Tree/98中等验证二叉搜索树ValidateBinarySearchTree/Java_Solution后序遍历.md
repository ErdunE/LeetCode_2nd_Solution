
## 后序遍历
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
        // 结果不是无穷大 如果是无穷大 就证明不是一个二叉搜索树
        return dfs(root)[1] != Long.MAX_VALUE;
    }
    // 先遍历左右子树，再判断节点值
    private long[] dfs(TreeNode node){
        // 判断边界条件
        if(node == null){
            return new long[]{Long.MAX_VALUE, Long.MIN_VALUE};
        }
        // 递归左指数，拿到左边最小值和左边最大值
        long[] left = dfs(node.left);
        // 递归右指数，拿到右边最小值和左边最大值
        long[] right = dfs(node.right);
        // 记录下节点值
        long x = node.val;
        
        // 如果该节点小于等于左边的最大值，或者大于等于右边的最小值，那么他就不是一个二叉搜索树
        // 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
        if(x <= left[1] || x >= right[0]){
            return new long[]{Long.MIN_VALUE, Long.MAX_VALUE};
        }
        // 返回左边的最小值和右边的最大值
        return new long[]{Math.min(left[0], x), Math.max(right[1], x)};
    }
}
```
前序遍历在某些数据下不需要递归到叶子节点就能返回（比如根节点左儿子的值大于根节点的值，左儿子就不会继续往下递归了），而中序遍历和后序遍历至少要递归到一个叶子节点。从这个角度上来说，前序遍历是最快的。   
中序遍历很好地利用了二叉搜索树的性质，使用到的变量最少。   
后序遍历的思想是最通用的，即自底向上计算子问题的过程。想要学好动态规划的话，请务必掌握自底向上的思想。

时间复杂度：O(n)，其中 n 为二叉搜索树的节点个数。   
空间复杂度：O(n)。最坏情况下，二叉搜索树退化成一条链，因此递归需要 O(n) 的栈空间。
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

    // 用一个全局变量保存最终的结果
    int res;
    // 用一个全局变量保存当前访问到第几个节点
    int count; 
    // 如果不使用全局变量，而是使用函数传参，需要注意「值传递」和「引用传递」的区别：
    // 值传递：每个递归的内部都需要对同一个变量修改，如果用普通函数的传参，对于 int 型的参数，使用的是值传递，即拷贝了一份传到了函数里面。那么函数里面对 int 型的修改不会影响外边的变量。
    // 使用全局变量，可以保证递归函数的每次修改都是反映到全局的，从而保证遍历到第 k 个的时候，所有的递归立刻停止。

    
    public int kthSmallest(TreeNode root, int k) {
        res = 0;
        count = k;
        dfs(root);
        return res;
    }

    public void dfs(TreeNode root){
        if(root == null){
            return;
        }
        dfs(root.left);
        count--;
        if(count == 0){
            res = root.val;
        }
        dfs(root.right);
    }
}
```

时间复杂度：O(H+k)，其中 H 为树的高度，因为需要递归找到最小的节点再开始数 k 个节点   
空间复杂度：O(H)，因为递归用了系统栈，而栈的深度最多只有树的高度




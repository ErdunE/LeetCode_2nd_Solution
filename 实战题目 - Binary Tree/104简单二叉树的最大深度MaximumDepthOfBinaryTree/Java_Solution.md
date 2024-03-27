```
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

找出终止条件：当前节点为空
找出返回值：节点为空时说明高度为 0，所以返回 0，节点不为空时则分别求左右子树的高度的最大值，同时加 1 表示当前节点的高度，返回该数值
某层的执行过程：在返回值部分基本已经描述清楚

时间复杂度：O(n),递归过程中每个节点都被遍历到
空间复杂度：O(n), 调用了额外的栈空间，栈的大小取决于二叉树的高度，二叉树最坏情况下的高度为 n


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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        preOrder(root, ans);
        return ans;
    }

    private void preOrder(TreeNode root, List<Integer> ans){
        if(root != null){
            ans.add(root.val);
            preOrder(root.left, ans);
            preOrder(root.right, ans);
        }
        return;
    }
}
```

时间复杂度: n为该二叉树的节点总数。每个节点都会被遍历(遍历方法以其为参数的执行次数)且只遍历一次，因此时间复杂度为O(n)。

空间复杂度: 空间复杂度取决于栈深，而栈深与该二叉树的形状有关，如果为链状，达到最大空间复杂度O(n)，如果为完全二叉树(complete binary tree)，栈深为O(logn)。


| 前序(根左右)                       | 中序(左根右)                     | 后序(左右根)                       |
| --------------------------------------- | ------------------------------------- | --------------------------------------- |
| res.add(root.val);                      | inorderTraversalCur(root.left, res);  | postorderTraversalCur(root.left, res);  |
| preorderTraversalCur(root.left, res);   | res.add(root.val);                    | postorderTraversalCur(root.right, res); |
| preorderTraversalCur(root.right, res);  | inorderTraversalCur(root.right, res); | res.add(root.val);                      |

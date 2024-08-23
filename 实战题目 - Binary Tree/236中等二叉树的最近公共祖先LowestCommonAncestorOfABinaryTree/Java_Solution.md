```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //如果根为空，或者只有一个p或者q值，即直接返回当前节点即可
        if(root == null || root == p || root == q){
            return root;
        }
        // 如果左子树找到p节点就不用继续递归了 直接返回
        // 然后再判断 ==> 如果此时右子树递归到最后都没有找到q 即null 则说明q在左子树, 且在左子树p点的下面
        // 所以直接返回之前返回的p节点就好了, 如果左右子树都找到了p或q, 则直接返回他们的共同的上一节点root
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if(left == null){
            return right;
        }
        if(right == null){
            return left;
        }
        return root;
    }
}
```

时间复杂度：O(n)，其中 n 为二叉树的节点个数。   
空间复杂度：O(n)。最坏情况下，二叉树是一条链，因此递归需要 O(n) 的栈空间。



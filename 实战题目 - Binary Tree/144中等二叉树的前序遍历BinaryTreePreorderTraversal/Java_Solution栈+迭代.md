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
        Deque<TreeNode> stack = new LinkedList<>();
        // 同时满足root不为空 且 栈不为空的时候 才返回结果
        while(root != null || !stack.isEmpty()){
            // root不为空的时候，向left方向持续推进直到子节点
            while(root != null){
                // 将root的val加入到结果中，满足前序“根左右”的顺序进行遍历
                ans.add(root.val);
                stack.push(root);
                root = root.left;
            }
            // 向left推进到子节点后弹出该子节点
            root = stack.pop();
            // 再向right推进，如果right也是null，那么回到一开始的while判断栈
            // 如不空，则跳过第二个while，再次弹出顶栈，也就是某节点的左子树遍历完毕，回到该节点
            root = root.right;
        }
        return ans;
    }
}
```

时间复杂度: n为该二叉树的节点总数。每个节点都会被遍历(遍历方法以其为参数的执行次数)且只遍历一次，因此时间复杂度为O(n)。

空间复杂度: 空间复杂度取决于栈深，而栈深与该二叉树的形状有关，如果为链状，达到最大空间复杂度O(n)，如果为完全二叉树(complete binary tree)，栈深为O(logn)。
               |

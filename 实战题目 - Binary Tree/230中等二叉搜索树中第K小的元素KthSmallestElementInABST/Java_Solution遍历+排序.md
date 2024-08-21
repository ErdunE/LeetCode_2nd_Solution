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
    // 创建数组来记录遍历的值
    List<Integer> list = new ArrayList<>();
    public int kthSmallest(TreeNode root, int k) {
        // 遍历整个root
        dfs(root);
        // 将遍历后的结果进行排序
        Collections.sort(list);
        // 返回第k个值
        return list.get(k - 1);
    }

    void dfs(TreeNode root){
        if(root == null){
            return;
        }
        list.add(root.val);
        dfs(root.left);
        dfs(root.right);
    }
}
```

时间复杂度：树的遍历时间复杂度为 O(n)；排序的复杂度为 O(nlogn)。整体复杂度为 O(nlogn)   
空间复杂度：O(n)  



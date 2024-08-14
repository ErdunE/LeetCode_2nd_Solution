DFS
```
class Solution {
    public TreeNode invertTree(TreeNode root) {
        // 递归函数的终止条件，节点为空时返回
        if(root == null){
            return null;
        }
        // 交换节点的左右子树
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = temp;

        // 递归交换当前节点的左子树
        invertTree(root.left);
        // 递归交换当前节点的右子树
        invertTree(root.right);

        // 当前节点的左右子树全部交换完了，返回节点
        return root;

    }
}
```

时间复杂度：每个节点都要访问一次，所以是O(n)    
空间复杂度：最坏的情况，需要存放O(h)个函数调用(h是树高)，所以是O(h)

BFS
```
class Solution {
    public TreeNode invertTree(TreeNode root) {
        // 递归函数的终止条件，节点为空时返回
        if(root == null){
            return null;
        }

        //将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while(!queue.isEmpty()){
            //每次都从队列中拿一个节点，并交换这个节点的左右子树
            TreeNode temp = queue.poll();
            TreeNode left = temp.left;
            temp.left = temp.right;
            temp.right = left;

            //如果当前节点的左子树不为空，则放入队列等待后续处理
            if(temp.left != null){
                queue.add(temp.left);
            }

            //如果当前节点的右子树不为空，则放入队列等待后续处理
            if(temp.right != null){
                queue.add(temp.right);
            }

        }
        return root;
    }
}
```
时间复杂度：每个节点都要访问一次，所以是O(n)    
空间复杂度：最坏的情况下会包含所有的叶子节点，完全二叉树叶子节点是 n/2个，所以时间复杂度是 0(n)
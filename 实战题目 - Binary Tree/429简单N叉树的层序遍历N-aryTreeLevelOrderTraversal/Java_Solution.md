```

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        // 创建一个数组来保存结果
        List<List<Integer>> res = new ArrayList<>();
        // 如果root为空直接返回空数组
        if(root == null){
            return res;
        }
        // 创建一个队列用来保存每个元素
        Queue<Node> queue = new LinkedList<>();
        // 先把root加入到队列中
        queue.add(root);

        // 队列一直循环知道队列为空
        while(!queue.isEmpty()){
            // 定义队列大小
            int queueSize = queue.size();
            // 每一层单独一个新的数组
            List<Integer> floor = new ArrayList<>();
            // 循环该队列大小并依次将元素的值加入到楼层数组中
            for(int i = 0; i < queueSize; i++){
                Node node = queue.poll();
                floor.add(node.val);
                // 将该元素的子元素加入到队列中等待下一轮的遍历 
                for(Node n : node.children){
                    queue.offer(n);
                }               
            }
            // 结果中加入当前层元素的值
            res.add(floor);
        }
        return res;
    }
}
```

时间复杂度：O(n)，其中 n 是树中包含的节点个数。在广度优先搜索的过程中，我们需要遍历每一个节点恰好一次。

空间复杂度：O(n)，即为队列需要使用的空间。在最坏的情况下，树只有两层，且最后一层有 n−1 个节点，此时就需要 O(n) 的空间。



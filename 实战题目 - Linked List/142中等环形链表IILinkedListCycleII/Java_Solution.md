```
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        ListNode pos = head;
        Set<ListNode> visited = new HashSet<ListNode>();

        while(pos != null){
            if(visited.contains(pos)){
                return pos;
            }else{
                visited.add(pos);
            }

            pos = pos.next;
        }

        return null;
    }
}
```

遍历链表中的每个节点，并将它记录下来；一旦遇到了此前遍历过的节点，就可以判定链表中存在环

时间复杂度：O(N)，其中 N 为链表中节点的数目。需要访问链表中的每一个节点。

空间复杂度：O(N)，其中 N 为链表中节点的数目。需要将链表中的每个节点都保存在哈希表当中。







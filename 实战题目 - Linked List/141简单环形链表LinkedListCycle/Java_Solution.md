### Solution 1 
```
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head == null){
            return false;
        }

        ListNode p = head;
        ListNode q = head.next;

        while(true){
            if(p == q){
                break;
            }else if(q == null || q.next == null || q.next.next == null){
                return false;
            }else{
                p = p.next;
                q = q.next.next;
            }
        }
        return true;
    }
}
```
### Solution 2
```
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head == null){
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while(slow != fast){
            if(fast == null || fast.next == null){
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}
```

慢指针针每次走一步，快指针每次走两步，如果相遇就说明有环，如果有一个为空说明没有环


时间复杂度：O(N) 链表节点数

空间复杂度：O(1) 除了两个指针并没有多占用空间


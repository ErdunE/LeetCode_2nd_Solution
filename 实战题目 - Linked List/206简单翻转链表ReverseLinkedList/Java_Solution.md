```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        ListNode tmp = null;

        while(cur != null){
            // 暂存后继节点 cur.next
            tmp = cur.next; 
            // 修改next引用指向
            cur.next = pre;
            pre = cur;
            // pre 暂存 cur
            cur = tmp;
            // cur 访问下一节点
        }

        return pre;
    }
}
```


时间复杂度：O(n)，遍历链表使用线性大小时间

空间复杂度：O(n)，遍历链表的递归深度达到 N ，系统使用 O(N) 大小额外空间。


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
    public ListNode swapPairs(ListNode head) {
        // 已有的链表加一个头部 head node
        ListNode resultHead = new ListNode();

        resultHead.next = head;

        // curNode 遍历链表时用
        ListNode curNode = resultHead;

        // 开始遍历链表
        while(curNode != null && curNode.next != null && curNode.next.next != null){
            ListNode f = curNode;
            ListNode s = curNode.next;
            ListNode t = s.next;

            // 两两交换链表结点
            f.next = t;
            s.next = t.next;
            t.next = s;

            // 标杆位后移2位
            curNode = curNode.next.next;
        
        }
        
        return resultHead.next;
    }
}
```
https://leetcode.cn/problems/swap-nodes-in-pairs/solutions/695513/yuan-lai-hui-luo-ji-qing-xi-jian-dan-yi-8t93h/

时间复杂度： 整个链表需要遍历一遍，所以算法时间复杂度的上限是 O(n)
空间复杂度： 不管链表有多长，运行算法需要额外开辟的空间总是常数级的，算法的空间复杂度是O(1)




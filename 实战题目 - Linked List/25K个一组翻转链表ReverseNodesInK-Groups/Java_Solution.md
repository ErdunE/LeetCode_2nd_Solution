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
    public ListNode reverseKGroup(ListNode head, int k) {
        // 此处只是设置一个哨兵节点
        ListNode dummy = new ListNode(0);
        // 哨兵节点的下一个结点指向首节点
        dummy.next = head;


        // 上阶段的最后一个结点，结点的初始化
        ListNode pre = dummy;
        // 本阶段的最后一个结点
        ListNode end = dummy;

        while(end.next != null){
            // 此处是为了找到其中的k个字结点
            for(int i = 0; i < k & end != null; i++){
                end = end.next;
            }
            // 如果直接到头了说明不满足k个子节点
            if(end == null){
                break;
            }


            // 此处是为了记录翻转始末的首结点
            ListNode start = pre.next;
            // 此处是为了记录下一阶段的起始点
            ListNode nextStart = end.next;

            // 此处是为了进行后面的翻转操作，断开此处链接，让后面翻转知道截断点在哪里
            end.next = null;
            // 翻转操作
            pre.next = reverse(start);

            // 反转之后，首节点实际上已经是最后一个结点了，为了和后面的划分链接，让其下一个结点，连接到下一个阶段的首节点
            start.next = nextStart;
            // pre再次来到下一阶段的上一个阶段 也就是本段的末尾结点
            pre = start;
            // 结束点，准备开始寻找下一个阶段的结束点
            end = pre;
            
        }

        // 返回哨兵
        return dummy.next;

    }
    

    // 交换操作
    private ListNode reverse(ListNode head){
        ListNode pre = null;
        ListNode curr = head;

        while(curr != null){
            ListNode next = curr.next;
            curr.next = pre;
            pre = curr;
            curr = next;
        }

        // 返回哨兵，此处是最新的翻转序列的起始点
        return pre;
    }
}


```

时间复杂度: O(n∗K) 最好的情况为 O(n) 最差的情况未 O(n^2)   
空间复杂度: O(1) 除了几个必须的节点指针外，我们并没有占用其他空间




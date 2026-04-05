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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode res = new ListNode();
        ListNode dummy = res;

        while(list1 != null && list2 != null) {
            if(list1.val > list2.val) {
                dummy.next = new ListNode(list2.val);
                list2 = list2.next;
            } else {
                dummy.next = new ListNode(list1.val);
                list1 = list1.next;
            }

            dummy = dummy.next;
        }

        ListNode remainder = list1 == null ? list2 : list1;

        dummy.next = remainder;

        return res.next;
    }
}
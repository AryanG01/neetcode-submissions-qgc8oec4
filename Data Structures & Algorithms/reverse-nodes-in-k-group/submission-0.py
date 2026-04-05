# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        def get_kth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            
            return node
        
        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            prev, cur = kth.next, group_prev.next
            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next
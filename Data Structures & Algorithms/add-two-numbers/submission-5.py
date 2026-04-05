# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            if val <= 9:
                head.next = ListNode(val)
                carry = 0
            else:
                head.next = ListNode(val - 10)
                carry = 1
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        remaining = None
        if l1:
            remaining = l1
        else:
            remaining = l2
        
        while remaining:
            val = remaining.val + carry
            if val <= 9:
                head.next = ListNode(val)
                carry = 0
            else:
                head.next = ListNode(val - 10)
                carry = 1
            head = head.next
            remaining = remaining.next
            
        if carry:
            head.next = ListNode(1)
        
        return res.next

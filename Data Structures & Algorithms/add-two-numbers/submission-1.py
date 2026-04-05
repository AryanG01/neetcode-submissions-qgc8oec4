# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0

        while l1 and l2:
            temp = l1.val + l2.val + carry
            if temp > 9:
                temp -= 10
                carry = 1
            else:
                carry = 0
            
            cur.next = ListNode(temp)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            remainder = l1
        else:
            remainder = l2
        
        while remainder:
            temp = remainder.val + carry
            if temp > 9:
                temp -= 10
                carry = 1
            else:
                carry = 0
            
            cur.next = ListNode(temp)
            cur = cur.next
            remainder = remainder.next
        
        if carry == 1:
            cur.next = ListNode(1)
            
        return res.next
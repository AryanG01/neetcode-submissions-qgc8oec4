# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #step 1 - find mid point
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2 - split them
        p1 = None
        p2 = slow.next
        slow.next = None
        
        #step 3 - reverse the second list
        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        
        second = p1

        #step 4 - merge the two list
        first = head
        
        while first and second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first, second = t1, t2


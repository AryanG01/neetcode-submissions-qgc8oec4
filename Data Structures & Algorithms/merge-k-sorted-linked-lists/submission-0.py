# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode()
        cur = dummy

        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, idx, l))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(min_heap, (cur.next.val, i, cur.next))
        
        return dummy.next

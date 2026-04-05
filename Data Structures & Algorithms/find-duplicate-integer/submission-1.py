class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (Cycle Detection) Algorithm

        Thought Process:
        - We treat the array like a linked list where each index points to the value at that index: i → nums[i].
        - Because there are n + 1 elements and values are from 1 to n, there must be a cycle (due to the pigeonhole principle).
        - The cycle is formed because the duplicate number causes multiple indices to point to the same value.
        - Floyd’s algorithm helps find the entry point of the cycle, which corresponds to the duplicate number.

        Steps:
        1. Use two pointers (slow and fast). Move slow by one step and fast by two steps.
           If they meet, a cycle exists.
        2. To find the cycle's entry point (duplicate), reset one pointer to the start.
           Move both pointers one step at a time until they meet again.
           That meeting point is the duplicate number.
        """

        # Step 1: Detect the cycle using slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find the entry point of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

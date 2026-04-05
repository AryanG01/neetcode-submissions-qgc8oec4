class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0

        for num in nums:
            if not num:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
        
        return max(max_count, count)
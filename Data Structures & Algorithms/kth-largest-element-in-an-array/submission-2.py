import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, len(nums) - k)
    
    def quickSelect(self, nums, k):
        pivot = nums[random.randrange(len(nums))]  # Simple pivot (add randomization for optimization)
        smaller, equal, larger = [], [], []
        
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        
        if k < len(smaller):
            return self.quickSelect(smaller, k)
        elif k < len(smaller) + len(equal):
            return pivot
        else:
            return self.quickSelect(larger, k - (len(smaller) + len(equal)))

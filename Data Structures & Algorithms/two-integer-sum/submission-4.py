class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}

        for i, n in enumerate(nums):
            if target - n in pos:
                return [pos[target - n], i]
            
            pos[n] = i

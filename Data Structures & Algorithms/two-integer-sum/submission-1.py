class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for idx, num in enumerate(nums):
            val = target - num
            if val in freq:
                return [freq[val], idx]
            else:
                freq[num] = idx
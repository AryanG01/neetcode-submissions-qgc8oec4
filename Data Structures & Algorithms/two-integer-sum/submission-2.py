class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            if target - nums[i] in pos:
                return [pos[target - nums[i]], i]
            else:
                pos[nums[i]] = i

        return [-1, -1]
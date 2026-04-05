class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for j in range(n):
            idx = abs(nums[j]) - 1
            if 0 <= idx < n:
                if nums[idx] > 0:
                    nums[idx] *= -1
                elif nums[idx] == 0:
                    nums[idx] = -1 * (len(nums) + 1)
        
        for k in range(1, len(nums) + 1):
            idx = k - 1
            if nums[idx] >= 0:
                return k
        
        return n + 1
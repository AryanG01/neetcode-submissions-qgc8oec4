class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == nums[r]:
                while r < len(nums) and nums[r] == nums[l]:
                    r += 1
                
                if r == len(nums):
                    break
                
                l += 1
                nums[l] = nums[r]
            else:
                l += 1
                nums[l] = nums[r]
                r += 1

        return l + 1
                
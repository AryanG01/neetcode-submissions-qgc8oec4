import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = 1
        res = [nums[0]]

        for i in range(1, len(nums)):
            if res[-1] < nums[i]:
                LIS += 1
                res.append(nums[i])
                continue
            
            temp = bisect.bisect_left(res, nums[i])
            res[temp] = nums[i]
        
        return LIS
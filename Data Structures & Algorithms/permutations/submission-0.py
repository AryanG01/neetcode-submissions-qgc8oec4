class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(cur, idx):
            if idx == len(nums):
                res.append(cur[:])
                return
            
            for i in range(idx, len(nums)):
                cur[i], cur[idx] = cur[idx], cur[i]
                helper(cur, idx + 1)
                cur[i], cur[idx] = cur[idx], cur[i]
        
        helper(nums, 0)
        return res

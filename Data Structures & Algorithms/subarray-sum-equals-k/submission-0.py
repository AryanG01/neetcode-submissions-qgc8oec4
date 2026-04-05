class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0

        prefixSum = {0 : 1}

        for num in nums:
            total += num
            diff = total - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[total] = prefixSum.get(total, 0) + 1
        
        return res
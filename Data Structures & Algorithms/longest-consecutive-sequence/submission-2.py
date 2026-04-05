class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = defaultdict(int)
        max_res = 0

        for num in nums:
            if not res[num]:
                res[num] = res[num - 1] + res[num + 1] + 1
                res[num - res[num - 1]] = res[num]
                res[num + res[num + 1]] = res[num]
                max_res = max(max_res, res[num])
        
        return max_res
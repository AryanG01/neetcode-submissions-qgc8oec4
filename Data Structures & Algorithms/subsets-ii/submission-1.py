class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def helper(start, path):
            res.add(tuple(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()
        
        helper(0, [])
        return [list(r) for r in res]
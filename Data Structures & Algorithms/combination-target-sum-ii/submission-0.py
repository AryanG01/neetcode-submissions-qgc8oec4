class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(i, cur, total):
            if total == target:
                res.append(cur[:])
                return

            for j in range(i, len(candidates)):
                if total > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                cur.append(candidates[j])
                helper(j + 1, cur, total + candidates[j])
                cur.pop()

        helper(0, [], 0)
        return res

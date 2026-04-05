class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        if n == 2:
            return k * k
        
        prev_same = k
        prev_diff = k * (k - 1)

        for i in range(3, n + 1):
            new_same = prev_diff
            new_diff = (prev_same + prev_diff) * (k - 1)

            prev_same, prev_diff = new_same, new_diff
        
        return prev_same + prev_diff
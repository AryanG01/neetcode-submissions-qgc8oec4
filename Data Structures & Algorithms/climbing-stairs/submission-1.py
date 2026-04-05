class Solution:
    # Top Down DP Approach
    def memoization(self, n, cache):
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.memoization(n - 1, cache) + self.memoization(n - 2, cache)
        return cache[n]

    def climbStairs(self, n: int) -> int:
        return self.memoization(n, {})
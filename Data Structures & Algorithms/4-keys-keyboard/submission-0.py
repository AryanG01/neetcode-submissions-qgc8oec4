class Solution:
    def maxA(self, n: int) -> int:
        if n <= 6:
            return n
        
        dp = [0] * (n + 1)

        for i in range(1, 7):
            dp[i] = i
        
        for i in range(7, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        
        return dp[n]
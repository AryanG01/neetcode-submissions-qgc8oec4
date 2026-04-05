class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 1000000007

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[2] = 1

        for i in range(4, n + 1, 2):
            for j in range(0, i, 2):
                dp[i] = (dp[i] + (dp[j] * dp[i - j - 2])) % MOD
        
        return dp[n]

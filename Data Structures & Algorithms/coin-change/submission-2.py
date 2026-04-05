class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        This function solves the classic Coin Change problem using dynamic programming.

        The idea is to build up a dp array where dp[i] represents the minimum number of coins
        needed to make up the amount i. We initialize dp with a value greater than any possible
        number of coins (amount + 1), and set dp[0] = 0 because zero coins are needed to make amount 0.

        For each coin denomination, we iterate through all amounts from coin to amount, and update dp[i]
        by taking the minimum of its current value and dp[i - coin] + 1. This represents choosing to use
        the current coin (which adds 1 coin to the count) and seeing if it leads to a better solution.

        After processing all coins, dp[amount] will contain the minimum number of coins needed to make
        up the target amount. If it's still equal to amount + 1, it means no combination of coins can
        produce the target amount, so we return -1.
        """
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount] != amount+1 else -1

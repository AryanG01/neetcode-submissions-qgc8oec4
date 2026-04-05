class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = float('inf')

        for i in range(len(prices)):
            low = min(low, prices[i])
            maxProfit = max(prices[i] - low, maxProfit)
        
        return maxProfit
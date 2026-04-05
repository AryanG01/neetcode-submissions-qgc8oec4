class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_res = 0

        for p in range(1, len(prices)):
            low = min(low, prices[p])
            max_res = max(max_res, prices[p] - low)
        
        return max_res
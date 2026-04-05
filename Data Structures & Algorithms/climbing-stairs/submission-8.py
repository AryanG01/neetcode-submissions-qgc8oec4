class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            temp = prev1 + prev2
            prev2 = prev1
            prev1 = temp
        
        return prev1 if n > 1 else prev2
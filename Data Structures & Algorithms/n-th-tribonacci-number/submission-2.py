class Solution:
    def tribonacci(self, n: int) -> int:
        prev3 = 0
        prev2 = 1
        prev1 = 1

        if n == 0:
            return prev3
        elif n == 1:
            return prev2
        elif n == 2:
            return prev1

        for i in range(3, n + 1):
            temp = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = temp
        
        return prev1

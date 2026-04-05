class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 1000000007

        # Size n + 1 so the index matches the number of people perfectly.
        # Initialize with -1 to differentiate from the mathematical answer 0.
        memo = [-1] * (n + 1)
        
        def f(n):
            # Base cases
            if n == 0:
                return 1
            if n == 1:
                return 0
            
            # $O(1)$ Memo lookup by index
            if memo[n] != -1:
                return memo[n]
            
            _sum = 0
            # Your flawless split logic
            for i in range(1, n, 2):
                left = f(i - 1)
                right = f(n - i - 1)
                _sum = (_sum + left * right) % MOD
            
            # Store at index n, return from index n
            memo[n] = _sum
            return memo[n]   
        
        return f(n)
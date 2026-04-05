class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        
        # We only need an array up to numPeople.
        dp = [0] * (numPeople + 1)
        
        # Base cases
        dp[0] = 1
        dp[2] = 1
        
        # Outer loop: i is the total number of people in our current subproblem.
        # We only care about even numbers of people (4, 6, 8... numPeople)
        for i in range(4, numPeople + 1, 2):
            
            # Inner loop: j is the number of people on the LEFT side of the handshake.
            # j must also be even (0, 2, 4... up to i-2)
            for j in range(0, i, 2):
                
                # Left side combinations * Right side combinations
                left_ways = dp[j]
                right_ways = dp[i - 2 - j]
                
                # Add this split's combinations to our total for dp[i], and apply modulo
                dp[i] = (dp[i] + (left_ways * right_ways)) % MOD
                
        return dp[numPeople]
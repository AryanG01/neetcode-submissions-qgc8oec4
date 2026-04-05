class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        max_pal = s[0]

        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if j - i + 1 > len(max_pal):
                        max_pal = s[i:j+1]
        
        return max_pal

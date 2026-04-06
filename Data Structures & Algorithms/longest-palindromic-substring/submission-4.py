class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        pal = s[0]
        max_pal = 1

        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if j - i + 1 > max_pal:
                        max_pal = j - i + 1
                        pal = s[i : j + 1]

        return pal
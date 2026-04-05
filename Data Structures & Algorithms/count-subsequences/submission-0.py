class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        ok so whats the recursive relation over here?
        if s[i] and t[j] are equal:
            we can either use this letter or skip it in case we encounter the same again
            so for the first case we would move both i and j pointers but for the latter
            would only move the i pointer coz we need to match t in s so u only move t
            pointer when u see a match
        else:
            if it dont match then repeat the latter half of the above part
        
        what are our base cases?
        if s == "a" and t == ""
        then it is a valid outcome coz a subsequence of s could be ""

        if its reversed t == "a" and s == ""
        then answer is 0 coz no way its happening

        so our dp table needs to be +1 in either dimension
        """

        len_s = len(s)
        len_t = len(t)

        dp = [[0] * (len_t + 1) for z in range(len_s + 1)]

        # my base case for the straight part
        for i in range(len_s + 1):
            dp[i][0] = 1
        
        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len_s][len_t]

    
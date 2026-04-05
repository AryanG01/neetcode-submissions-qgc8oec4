class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        so hint its a 1d dp question

        We can use a boolean array to keep track of whether upto a certain index of the
        string can be segmented into words from the wordDict

        we can let dp[i] be true if the substring s[0:i], the first i characters of s,
        can be split into words that are in the dictionary

        but how do we check if dp[i] = True?
        we can check all possible iteration points j, from start to i, and check whether
        dp[j] is True and s[j:i] is a valid word, so we break it up to see is there any
        particular index which comprises of valid words and whether from that index to 
        our index is a valid word

        dp[i] = dp[j] and s[j:i]

        Base Case: dp[0] = True
        """
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True

        return dp[n]
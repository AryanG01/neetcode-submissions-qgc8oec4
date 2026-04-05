class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        res, count = 0, 0
        start = 0

        for i in range(len(s)):
            if s[i] in freq and freq[s[i]] >= start:
                res = max(res, count)
                start = freq[s[i]] + 1
                count = i - start + 1
            else:
                count += 1

            freq[s[i]] = i

        return max(res, count)
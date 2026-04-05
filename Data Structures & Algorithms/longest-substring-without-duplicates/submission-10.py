class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        l = 0
        length = 0
        max_len = 0

        for r in range(len(s)):
            if s[r] not in pos or pos[s[r]] < l:
                pos[s[r]] = r
                length += 1
                continue
            
            max_len = max(max_len, length)
            l = pos[s[r]] + 1
            length = r - l + 1
            pos[s[r]] = r

        return max(max_len, length)


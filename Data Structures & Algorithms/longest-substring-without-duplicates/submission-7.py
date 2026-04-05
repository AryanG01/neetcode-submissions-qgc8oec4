class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        length = 0
        max_len = 0
        start = 0

        for i in range(len(s)):
            if s[i] not in pos or (pos[s[i]] < start):
                pos[s[i]] = i
                length += 1
                continue
            
            max_len = max(max_len, length)
            start = pos[s[i]] + 1
            length = i - start + 1
            pos[s[i]] = i
        
        return max(max_len, length)



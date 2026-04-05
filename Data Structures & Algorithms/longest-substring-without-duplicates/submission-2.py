class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        res = 0
        count = 0
        start = 0
        i = 0

        for c in s:
            if c in pos and pos[c] >= start:
                res = max(res, count)
                start = pos[c] + 1
                count = i - start + 1
            else:
                count += 1
            
            pos[c] = i
            i += 1
        
        return max(res, count)
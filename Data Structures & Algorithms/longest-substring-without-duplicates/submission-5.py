class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = defaultdict(int)
        max_length = 0
        length = 0
        start = 0

        for i in range(len(s)):
            if (s[i] not in pos) or (s[i] in pos and pos[s[i]] < start):
                pos[s[i]] = i
                length += 1
                continue
            
            max_length = max(max_length, length)
            start = pos[s[i]] + 1
            length = i - start + 1
            pos[s[i]] = i
        
        return max(max_length, length)

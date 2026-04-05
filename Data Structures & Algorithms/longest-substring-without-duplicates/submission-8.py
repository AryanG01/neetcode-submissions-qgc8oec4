class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        window = {}
        length = 0
        max_length = 0

        while end < len(s):
            if s[end] not in window or window[s[end]] == -1:
                window[s[end]] = end
                length += 1
                end += 1
            else:
                while start <= window[s[end]]:
                    window[s[start]] = -1
                    length -= 1
                    start += 1
                window[s[end]] = end
                length += 1
                end += 1
            max_length = max(max_length, length)
        return max_length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Implement something like a sliding window approach, bu tthe window isnt
        of consistent size coz need resize when we encounter duplicate

        Instead of restarting window element by element keep track when its first
        occurenece happened and minus from current length + update its pos to
        latest pos
        """
        pos = {}
        res, count = 0, 0
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
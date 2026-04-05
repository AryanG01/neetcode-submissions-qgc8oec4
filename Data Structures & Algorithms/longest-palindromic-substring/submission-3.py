class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1 : r]
        
        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > max_len:
                res = p1
                max_len = len(p1)
            
            p2 = expand(i, i+1)
            if len(p2) > max_len:
                res = p2
                max_len = len(p2)
        
        return res

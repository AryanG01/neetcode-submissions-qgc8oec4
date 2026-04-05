class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        def expand(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            
            return res
        
        for i in range(n):
            res += expand(i, i)
            res += expand(i, i+1)
        
        return res
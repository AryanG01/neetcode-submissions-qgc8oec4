class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        memo = {}
        def helper(s):
            if s == "":
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            if s in memo:
                return memo[s]
            
            res = helper(s[1:])
            if int(s[:2]) <= 26:
                res += helper(s[2:])
            
            memo[s] = res
            return res
        
        return helper(s)
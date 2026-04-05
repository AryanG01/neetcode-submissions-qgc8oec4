class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}

        for c in t:
            if c not in freq_t:
                freq_t[c] = 0
            
            freq_t[c] += 1
        
        cur = 0
        req = len(freq_t)

        res = [0, 999]
        res_len = 1000

        window = {}

        l = 0

        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 0
            
            window[s[r]] += 1
            
            if s[r] in freq_t and freq_t[s[r]] == window[s[r]]:
                cur += 1
            
            while cur == req:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                if s[l] in freq_t and freq_t[s[l]] == window[s[l]]:
                    cur -= 1
                
                window[s[l]] -= 1

                l += 1

        return "" if res_len == 1000 else s[res[0] : res[-1] + 1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # A window to keep track of how many letters we need minimally
        freq_t = {}

        for c in t:
            if c not in freq_t:
                freq_t[c] = 0
            
            freq_t[c] += 1
        
        # Terminating Condition
        res = [0, 1000]
        res_len = 1001

        # Counter to see how many letters meet the requirement
        cur = 0
        req = len(freq_t)

        # A window to keep track of the letters we encounter
        window = {}

        l = 0

        for r, c in enumerate(s):
            if c not in window:
                window[c] = 0 
            
            window[c] += 1

            if c in freq_t and freq_t[c] == window[c]:
                cur += 1
            
            while cur == req:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
            
                if s[l] in freq_t and freq_t[s[l]] == window[s[l]]:
                    cur -= 1
                
                window[s[l]] -= 1

                l += 1
        
        return "" if res_len == 1001 else s[res[0]: res[-1] + 1]


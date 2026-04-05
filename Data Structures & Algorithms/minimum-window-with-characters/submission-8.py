class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_t = defaultdict(int)

        for c in t:
            cur_t[c] += 1
        
        cur = 0
        req = len(cur_t)

        cur_s = defaultdict(int)

        l = 0
        res_domain = [0, 999]
        res_len = 1000

        for idx, r in enumerate(s):
            cur_s[r] += 1
            if r in cur_t and cur_s[r] == cur_t[r]:
                cur += 1
            
            while cur == req:
                if (idx - l + 1) < res_len:
                    res_domain = [l, idx]
                    res_len = idx - l + 1
                
                if s[l] in cur_t and cur_t[s[l]] == cur_s[s[l]]:
                    cur -= 1
                
                cur_s[s[l]] -= 1
                l += 1
    
        return "" if res_len == 1000 else s[res_domain[0]:res_domain[1] + 1]






        

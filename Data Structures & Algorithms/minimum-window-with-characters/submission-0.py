class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Since t can be of variable length we need a dictionary to keep track of the
        letters and their frequencies.

        the idea is to have a window with variable size that can increase to allow 
        more letters to ensure we have at least as many characters as required in t
        and decrease to find the shortest possible substring by removing the leftmost
        character

        so we will need a cur variable and a req variable to keep track of how many
        of t do we have and how many more do we need. 
        
        Optimization - Instead of keeping track of the number of letters we can look at
        it from a higher level we take it as if we have letter c if the current freq in
        the string s matches its freq in string t

        we will need a result to keep track of best l and r and a result_len to help
        get shorter substrings and to help in the return condition

        """
        freq_t = {}

        for c in t:
            if c not in freq_t:
                freq_t[c] = 0
            
            freq_t[c] += 1
        
        window = {}

        cur = 0
        req = len(freq_t)

        result = [0, 9999]
        result_len = 100000

        l = 0

        for r in range(len(s)):
            c = s[r]

            if c not in window:
                window[c] = 0
            
            window[c] += 1

            if c in freq_t and freq_t[c] == window[c]:
                cur += 1

            while cur == req:
                if (r - l + 1 < result_len):
                    result = [l, r]
                    result_len = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    cur -= 1
            
                l += 1
        
        l, r = result

        return "" if result_len == 100000 else s[l:r+1]
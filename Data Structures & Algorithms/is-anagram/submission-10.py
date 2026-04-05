class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s) 
        len_t = len(t)
        if len_s != len_t:
            return False
        
        t_map = [0] * 26
        s_map = [0] * 26

        for i in range(len_s):
            s_map[ord(s[i]) - ord('a')] += 1
            t_map[ord(t[i]) - ord('a')] += 1
        
        return t_map == s_map
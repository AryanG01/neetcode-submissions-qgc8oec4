class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        s = ""

        while s1 and s2:
            s += s1[0] + s2[0]
            s1 = s1[1:]
            s2 = s2[1:]
        
        if s1:
            return s + s1
        else:
            return s + s2
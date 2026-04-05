class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False

        s1_d = [0] * 26
        s2_d = [0] * 26

        for i in range(l1):
            s1_d[ord(s1[i]) - ord('a')] += 1
            s2_d[ord(s2[i]) - ord('a')] += 1
        
        if s1_d == s2_d:
            return True
        
        for j in range(l1, l2):
            s2_d[ord(s2[j - l1]) - ord('a')] -= 1
            s2_d[ord(s2[j]) - ord('a')] += 1

            if s1_d == s2_d:
                return True
        
        return False
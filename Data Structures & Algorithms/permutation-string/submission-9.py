class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False
        
        f1 = [0] * 26
        f2 = [0] * 26

        for i in range(l1):
            f1[ord(s1[i]) - ord('a')] += 1
            f2[ord(s2[i]) - ord('a')] += 1
        
        if f1 == f2:
            return True
        
        for i in range(l1, l2):
            f2[ord(s2[i - l1]) - ord('a')] -= 1
            f2[ord(s2[i]) - ord('a')] += 1

            if f1 == f2:
                return True
        
        return False
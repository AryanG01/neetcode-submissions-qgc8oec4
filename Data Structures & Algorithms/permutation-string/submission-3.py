class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Since there are no connections between the lengths of s1 and s2, we need to check
        if s1 <= s2 before we start

        i am thinking of an iterative approach where we just start going until we 
        find a character that exists in s1, once we find it we compare a set of the next
        len(s2) - 1 characters starting from the letter we are at with a set of s1 and see
        if they are equal
        """
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:len1])
        
        if window == count_s1:
            return True
        
        for i in range(len1, len2):
            window[s2[i]] += 1
            
            window[s2[i - len1]] -= 1
            
            if window[s2[i - len1]] == 0:
                del window[s2[i - len1]]
            
            if window == count_s1:
                return True

        return False
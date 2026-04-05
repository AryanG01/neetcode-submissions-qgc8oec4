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

        if len(s1) > len(s2):
            return False

        word = sorted(s1)
        
        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in word:
                if sorted(s2[i:i+len(s1)]) == word:
                    return True
        
        return False


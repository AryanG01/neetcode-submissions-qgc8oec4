class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s) - 1):
            newS = s[:i] + s[i + 1:]
            if newS == newS[::-1]:
                return True

        return False
class Solution:
    """
    We need to find all ways to split a given string s into smaller parts such that 
    each part is a palindrome.

    we need to try different ways to split the word

    We can begin at an index start and try to form sub-palindromes from there. If we 
    reach the end of the string, we add the current temp result to the final result

    We go through all possible substrings starting at start. If a substring is a 
    palindrome, we add it to the list and continue checking the remaining part of 
    the string.

    When we finish checking a path, we remove the last added substring and try other 
    possibilities.
    """
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return result

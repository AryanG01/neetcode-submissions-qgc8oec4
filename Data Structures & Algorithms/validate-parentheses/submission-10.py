class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = len(s)

        if l % 2 != 0:
            return False

        for i in range(l):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        return not stack


        
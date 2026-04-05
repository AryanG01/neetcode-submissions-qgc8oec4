class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0

        while s_ptr < len(s) and p_ptr < len(p):
            if p[p_ptr] == ".":
                s_ptr += 1
                p_ptr += 1
                continue

            elif p[p_ptr] == "*":

                if self.isMatch(s[s_ptr:], p[p_ptr+1:]):
                    return True

                while s_ptr < len(s) and (p[p_ptr-1] == '.' or s[s_ptr] == p[p_ptr-1]):
                    s_ptr += 1
                    if self.isMatch(s[s_ptr:], p[p_ptr+1:]):
                        return True
                return False

            else:
                if s_ptr < len(s) and p[p_ptr] == s[s_ptr]:
                    s_ptr += 1
                    p_ptr += 1
                elif p_ptr < len(p) - 1 and p[p_ptr + 1] == "*":
                    p_ptr += 2
                else:
                    return False

        while p_ptr + 1 < len(p) and p[p_ptr + 1] == "*":
            p_ptr += 2

        return s_ptr == len(s) and p_ptr == len(p)

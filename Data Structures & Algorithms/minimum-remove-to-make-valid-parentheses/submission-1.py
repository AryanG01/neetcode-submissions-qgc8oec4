class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        oc = cc = 0

        for c in s:
            cc += c == ")"
        
        res = []
        for c in s:
            if c == "(":
                if oc == cc:
                    continue
                oc += 1
            elif c == ")":
                cc -= 1
                if oc == 0:
                    continue
                oc -= 1
            res.append(c)
        return "".join(res)
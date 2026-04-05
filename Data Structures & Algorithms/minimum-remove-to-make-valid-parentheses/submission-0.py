class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cc = oc = 0

        for c in s:
            if c == ")":
                cc += 1
        
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
            

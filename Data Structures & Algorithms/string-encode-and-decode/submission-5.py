class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}_{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                l += s[i]
            else:
                l = int(l)
                res.append(s[i + 1 : i + 1 + l])
                i += l
                l = ""
            i += 1
        
        return res
                

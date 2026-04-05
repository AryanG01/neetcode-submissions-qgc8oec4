class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}_{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = "" 
        while i < len(s):
            if s[i].isdigit():
                length += s[i]
            else:
                l = int(length)
                res.append(s[i+1: i+1+l])
                i += (l)
                length = ''
            i += 1
        
        return res


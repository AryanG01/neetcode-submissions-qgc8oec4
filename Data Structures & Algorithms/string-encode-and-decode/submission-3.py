class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}_{s}"
        
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        length = ""
        i = 0

        while i < len(s):
            if s[i] != "_":
                length += s[i]
            else:
                length = int(length)
                res.append(s[i+1 : i + length + 1])
                i += length
                length = ""
            i += 1
        
        return res
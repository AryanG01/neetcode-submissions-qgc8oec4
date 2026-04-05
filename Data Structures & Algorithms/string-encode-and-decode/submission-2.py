class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "_" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        delimitter = True
        length = 0

        while i < len(s):
            if s[i:i+2] == "0_":
	            res.append("")
	            i += 2
	            continue
            if delimitter:
                temp2 = ""
                while s[i] != "_":
                    temp2 += s[i]
                    i += 1
                length = int(temp2)
                i += 1
                delimitter = False
            else:
                res.append(s[i : i + length])
                i += length
                delimitter = True

        return res

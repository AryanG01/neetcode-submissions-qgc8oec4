class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f'{len(s)}_{s}'
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num = ''
        i = 0

        while i < len(s):
            if s[i] != '_':
                num += s[i]
                i += 1
            else:
                num = int(num)
                res.append(s[i+1 : i+1+num])
                i = i + 1 + num
                num = ''
        
        return res
            


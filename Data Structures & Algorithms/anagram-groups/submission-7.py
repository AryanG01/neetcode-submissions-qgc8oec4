class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in col:
                col[sorted_s] = [s]
            else:
                col[sorted_s].append(s)
        
        return list(col.values())
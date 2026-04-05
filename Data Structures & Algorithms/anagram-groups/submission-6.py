class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            s_arr = tuple(sorted(s))
            print(s_arr)
            dic[s_arr].append(s)
        
        return list(dic.values())
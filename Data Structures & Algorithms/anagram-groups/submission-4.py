class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for str in strs:
            mapping["".join(sorted(str))].append(str)
        
        return list(mapping.values())

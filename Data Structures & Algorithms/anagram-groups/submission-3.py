class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            print(sorted(s))
            mapping[tuple(sorted(s))].append(s)
        
        return list(mapping.values())
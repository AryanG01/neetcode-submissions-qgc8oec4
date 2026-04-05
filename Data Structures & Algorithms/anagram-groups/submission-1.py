class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            word = "".join(sorted(string))
            hashmap[word].append(string)
        
        return list(hashmap.values())
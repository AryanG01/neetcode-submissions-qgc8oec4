class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            temp = "".join(sorted(word))
            hashmap[temp].append(word)
        
        return list(hashmap.values())
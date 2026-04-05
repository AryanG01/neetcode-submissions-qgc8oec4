class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))
            anagram_list[word].append(s)
        
        return list(anagram_list.values())
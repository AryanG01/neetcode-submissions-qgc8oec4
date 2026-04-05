class Trie:

    def __init__(self):
        self.hashmap = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.hashmap:
                cur.hashmap[c] = Trie()
            cur = cur.hashmap[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            if idx == len(word):
                return root.endOfWord

            for c in range(idx, len(word)):
                if word[c] != ".":
                    if word[c] not in root.hashmap:
                        return False
                    root = root.hashmap[word[c]]
                    return dfs(idx + 1, root)
                else:
                    for i in root.hashmap.values():
                        if dfs(c + 1, i):
                            return True
                    return False
            
            return root.endOfWord
        
        return dfs(0, self.root)
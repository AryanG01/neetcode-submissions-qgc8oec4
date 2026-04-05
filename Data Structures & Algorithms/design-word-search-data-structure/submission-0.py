class WordDictionary:

    def __init__(self):
        self.store = []

    def addWord(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue
                
            flag = True
            for i, c in enumerate(w):
                if c == word[i] or word[i] == ".":
                    continue
                else:
                    flag = False
                    break
            
            if flag:
                return True
        
        return False

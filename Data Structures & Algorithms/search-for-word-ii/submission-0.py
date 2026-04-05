class Trie:

    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.word = word
        
        rows = len(board)
        cols = len(board[0])
        ans = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children.get(ch)

            if not node:
                return 
            
            if node.word:
                ans.append(node.word)
                node.word = None
            
            board[r][c] = "#"

            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, node)
            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, node)
            if r < rows - 1 and board[r + 1][c] != "#":
                dfs(r + 1, c, node)
            if c < cols - 1 and board[r][c + 1] != "#":
                dfs(r, c + 1, node)
            
            board[r][c] = ch

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return ans
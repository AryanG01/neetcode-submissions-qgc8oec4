class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in rows[row] or board[row][col] in cols[col]:
                    return False
                
                if board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                
                rows[row].append(board[row][col])
                cols[col].append(board[row][col])
                squares[(row // 3, col // 3)].append(board[row][col])

        return True
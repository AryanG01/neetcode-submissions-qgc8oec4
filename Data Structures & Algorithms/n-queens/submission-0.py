class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols_used = set()
        diags_used = set()
        adiags_used = set()
        placement = [-1] * n

        def place(row):
            if row == n:
                board = []
                for i in range(n):
                    c = placement[i]
                    board.append("." * c + "Q" + "." * (n - (c + 1)))
                res.append(board)
                return
            
            for c in range(n):
                d = row - c
                a = row + c

                if c in cols_used or d in diags_used or a in adiags_used:
                    continue
                
                placement[row] = c
                cols_used.add(c)
                diags_used.add(d)
                adiags_used.add(a)

                place(row + 1)

                placement[row] = -1
                cols_used.remove(c)
                diags_used.remove(d)
                adiags_used.remove(a)
        
        place(0)
        return res


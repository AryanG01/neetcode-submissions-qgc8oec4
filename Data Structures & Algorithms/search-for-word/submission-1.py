class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        probably a dfs solution

        u start searching for the first letter that matches and then choose one of the
        4 cardinal directions continue checking if the letters are correct and repeat 
        so on so forth

        need to do backtracking in case the letters dont match anymore
        """
        rows = len(board)
        cols = len(board[0])

        def valid(r, c, index):
            return 0 <= r < rows and 0 <= c < cols and word[index] == board[r][c] and board[r][c] != '-'

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if not valid(row, col, index):
                return False
            
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
            result = False
            board[row][col] = '-'

            for dx, dy in directions:
                result = result or dfs(row + dx, col + dy, index + 1)
                if result:
                    break

            board[row][col] = word[index]

            return result
            

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
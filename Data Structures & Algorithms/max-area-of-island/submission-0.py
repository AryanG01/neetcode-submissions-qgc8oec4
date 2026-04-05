class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) 
        
        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = max(area, dfs(row, col))
        
        return area

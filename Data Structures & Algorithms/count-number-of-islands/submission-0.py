from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"  # mark as visited
            while q:
                i, j = q.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = i + di, j + dj
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = "0"  # mark as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
                    
        return islands

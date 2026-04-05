from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Use a BFS approach to expand in all 4 cardinal directions to see if we can
        get to the treasure chest; the level marks the distance to the treasure chest.

        Ok for some reason the above shit doesnt work but feels too slow
        maybe it would be better to start from treasure chest and make our way out in
        4 cardinal directions and update wherever the value is INF with the distance till
        this point which we can keep track in the deque tgt with the row, col
        """
            
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        INF = 2147483647
        
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))
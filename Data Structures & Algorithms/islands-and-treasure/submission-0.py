from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Use a multi-source BFS approach starting from all treasure chests
        to find the minimum distance from each land cell to its nearest treasure chest.
        """
        if not grid or not grid[0]:
            return
            
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
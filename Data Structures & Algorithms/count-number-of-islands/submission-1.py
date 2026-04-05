from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Can we implement bfs to fidn the boundaries and mark all the connected Ones to keep track of islands?

        So the moment we find a 1 whiel traversing the array we see all its connected neighbours (4 cardinal
        directions + check to see if we went outside). Go and mark them in visited as well coz we visited them 
        during bfs traversal

        We need a data structure where we can insert soemthing in back and remove from front, liek a priority 
        queue in java just in this case dont need priority --google--> dequeue
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0" 
            while q:
                r, c = q.popleft()
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + x, c + y
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
                    
        return islands

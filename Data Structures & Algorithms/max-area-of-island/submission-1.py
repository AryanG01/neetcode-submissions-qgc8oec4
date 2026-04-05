class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            res = 1
            pq = deque([(r, c)])
            grid[r][c] = 0

            while pq:
                row, col = pq.popleft()
                for dx, dy in directions:
                    if 0 <= row + dx < rows and 0 <= col + dy < cols and grid[row + dx][col + dy] == 1:
                        res += 1
                        pq.append((row + dx, col + dy))
                        grid[row + dx][col + dy] = 0
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        
        return max_area
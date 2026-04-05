class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            pq = deque([(r, c)])

            while pq:
                row, col = pq.popleft()
                grid[row][col] = "*"

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dx, dy in directions:
                    if 0 <= row + dx < rows and 0 <= col + dy < cols and grid[row + dx][col + dy] == "1":
                        pq.append((row + dx, col + dy))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1
        
        return ans
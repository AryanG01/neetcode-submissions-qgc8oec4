class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            pq = deque([(r, c, 0)])

            while pq:
                row, col, dist = pq.popleft()
                grid[row][col] = dist
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dx, dy in directions:
                    if 0 <= row + dx < rows and 0 <= col + dy < cols and grid[row + dx][col + dy] != 0 and grid[row + dx][col + dy] != -1: 
                        if grid[row + dx][col + dy] > dist + 1 or grid[row + dx][col + dy] == INF:
                            pq.append((row + dx, col + dy, dist + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)

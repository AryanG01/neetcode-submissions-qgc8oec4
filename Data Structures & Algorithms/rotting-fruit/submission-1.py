class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            
            res += 1

        return res if fresh == 0 else -1
public class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int fresh = 0;
        int minutes = 0;
        LinkedList<int[]> rotten = new LinkedList<> (); 

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++){
                if (grid[i][j] == 1) {
                    fresh += 1;
                } else if (grid[i][j] == 2) {
                    rotten.add(new int[]{i, j});
                }
            }
        }

        if (fresh == 0) {
            return 0;
        }

        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (!rotten.isEmpty()) {
            int size = rotten.size();
            boolean changed = false;

            for (int temp = 0; temp < size; temp++) {
                int[] pos = rotten.poll();
                int x = pos[0];
                int y = pos[1];
                for (int[] dir : directions) {
                    int nx = x + dir[0];
                    int ny = y + dir[1];
                    
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        rotten.add(new int[]{nx, ny});
                        fresh--;
                        changed = true;
                    }
                }
            }
            if (changed) {
                    minutes++;
            }
        }
        
        // If there are still fresh oranges left, return -1
        return fresh > 0 ? -1 : minutes;
    }
}
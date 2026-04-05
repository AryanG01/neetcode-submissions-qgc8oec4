class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int start_row = 0;
        int end_row = matrix.length - 1;
        int mid_row = 0;
        
        boolean success_row = false;

        while(start_row <= end_row) {
            mid_row = end_row + (start_row - end_row) / 2;

            if(matrix[mid_row][0] <= target && matrix[mid_row][matrix[0].length - 1] >= target){
                success_row = true;
                break;
            } else if (matrix[mid_row][0] > target) {
                end_row = mid_row - 1;
            } else if (matrix[mid_row][matrix[0].length - 1] < target) {
                start_row = mid_row + 1;
            }
        }

        if(!success_row){
            return false;
        }

        int start_col = 0;
        int end_col = matrix[0].length - 1;

        while(start_col <= end_col) {
            int mid_col = end_col + (start_col - end_col) / 2;

            if(matrix[mid_row][mid_col] == target) {
                return true;
            } else if (matrix[mid_row][mid_col] > target) {
                end_col = mid_col - 1;
            } else {
                start_col = mid_col + 1;
            }
        }

        return false;
    }
}

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_l = 0
        r_h = len(matrix) - 1

        while r_l <= r_h:
            r_m = r_l + (r_h - r_l) // 2

            if target > matrix[r_m][-1]:
                r_l = r_m + 1
            else:
                r_h = r_m - 1
        
        row = r_l
        if row >= len(matrix) or target < matrix[row][0] or target > matrix[row][-1]:
            return False

        c_l = 0
        c_h = len(matrix[0]) - 1

        while c_l <= c_h:
            c_m = c_l + (c_h - c_l) // 2

            if target == matrix[row][c_m]:
                return True
            elif target > matrix[row][c_m]:
                c_l = c_m + 1
            else:
                c_h = c_m - 1
        
        return False

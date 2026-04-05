class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1 2 3 original
        4 5 6
        7 8 9

        Transpose
        1 4 7 
        2 5 8
        3 6 9

        flip along central y axis
        7 4 1
        8 5 2
        9 6 3
        """
        row = len(matrix)
        col = len(matrix[0])

        def transpose():
            for i in range(row):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def flip():
            for i in range(row):
                for j in range(col // 2):
                    matrix[i][j], matrix[i][row - 1 - j] = matrix[i][row - 1 - j], matrix[i][j]
        
        transpose()
        flip()

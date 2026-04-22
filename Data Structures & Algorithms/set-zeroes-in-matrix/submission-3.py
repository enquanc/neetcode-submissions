class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = []
        col_zero = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row_zero.append(row)
                    col_zero.append(col)

        for r in row_zero:
            for i in range(len(matrix[r])):
                matrix[r][i] = 0
        for c in col_zero:
            for j in range(len(matrix)):
                matrix[j][c] = 0
        
        
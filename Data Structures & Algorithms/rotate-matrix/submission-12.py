class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(0,i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        # Reverse
        matrix[:] = [row[::-1] for row in matrix]
        # for row in matrix:
        #     row.reverse()
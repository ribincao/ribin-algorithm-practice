class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        for i in range(n - 2, -1, -1):
            for j in range(m):
                tmp = matrix[i][j]
                matrix[i][j] += matrix[i + 1][j]
                if j > 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j - 1] + tmp)
                if j < m - 1:
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j + 1] + tmp)
        return min(matrix[0])


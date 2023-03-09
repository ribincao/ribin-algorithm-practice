class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [], []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    break
        
        for i in range(m):
            for j in range(n):
                if matrix[j][i] == 0:
                    cols.append(i)
                    break
        
        # print(rows, cols)
        for row in rows:
            for col in range(m):
                matrix[row][col] = 0
        
        for col in cols:
            for row in range(n):
                matrix[row][col] = 0

        

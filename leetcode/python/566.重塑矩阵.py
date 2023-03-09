class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        if m == 0:
            return mat
        n = len(mat[0])
        if n == 0:
            return mat
        if m * n != r * c:
            return mat
        
        rows = [0 for _ in range(c)]
        ret = [list(rows) for _ in range(r)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                row = idx // c
                col = idx % c
                ret[row][col] = mat[i][j]
        return ret
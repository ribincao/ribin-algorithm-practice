class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ret = 0
        n = len(triangle)
        if not triangle:
            return ret
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        
        
        return triangle[0][0]
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if(len(matrix) == 0): return False
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m - 1

        while row < n and col >= 0:
            search = matrix[row][col]
            if search == target:
                return True
            elif search < target:
                row += 1
            else:
                col -= 1
        return False
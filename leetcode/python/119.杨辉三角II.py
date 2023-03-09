class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d = {0: [1], 1: [1, 1]}
        if rowIndex in d:
            return d[rowIndex]
        
        tmp = self.getRow(rowIndex - 1)
        ret = [1 for _ in range(rowIndex + 1)]
        for i in range(1, rowIndex):
            ret[i] = tmp[i] + tmp[i - 1]
        d[rowIndex] = ret
        return ret
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []

        for i in range(numRows):
            tmp = [1 for _ in range(i + 1)]
            for j in range(1, len(tmp) - 1):
                tmp[j] = ret[-1][j] + ret[-1][j - 1]
            ret.append(tmp)
        return ret
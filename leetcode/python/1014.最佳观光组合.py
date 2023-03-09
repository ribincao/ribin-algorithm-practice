class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """ ret = (values[i] + i) + (values[j] - j)"""
        n = len(values)
        table_ = [values[i] - i for i in range(n)]
        table = [values[i] + i for i in range(n)]
        ret = 0
        tmp = table[0]
        for i in range(1, n):
            ret = max(ret, tmp + table_[i])
            tmp = max(tmp, table[i])
        return ret
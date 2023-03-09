class Solution:
    d = {0: 1, 1: 1}
    def numTrees(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        ret = 0
        for i in range(1, n + 1):
            left, right = i - 1, n - i
            ret += self.numTrees(left) * self.numTrees(right)
        self.d[n] = ret
        return ret
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ret = 0
        for i in range(1, n + 1):
            n -= i
            if n < 0:
                return ret
            ret += 1
        return ret

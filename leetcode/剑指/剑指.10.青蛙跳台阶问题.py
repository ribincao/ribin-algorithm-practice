class Solution:
    Ways = {0: 1, 1: 1}
    def numWays(self, n: int) -> int:
        if n in self.Ways:
            return self.Ways[n]
        self.Ways[n] = (self.numWays(n - 1) + self.Ways[n - 2]) % 1000000007
        return self.Ways[n]
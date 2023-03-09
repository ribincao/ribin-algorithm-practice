class Solution:
    FibNums = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n in self.FibNums:
            return self.FibNums[n]
        self.FibNums[n] = (self.fib(n - 1) + self.fib(n - 2)) % 1000000007
        return self.FibNums[n]
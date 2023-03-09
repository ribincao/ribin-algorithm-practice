class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0, 1, 1]
        for i in range(3, n + 1):
            num = sum(d[-3:])
            d.append(num)
            if i == n:
                return num
        return d[n]
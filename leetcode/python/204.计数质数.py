class Solution:
    def countPrimes(self, n: int) -> int:
        ret = 0
        Primes = [1 for _ in range(n)]

        for i in range(2, n):
            if Primes[i]:
                ret += 1
                for j in range(i * i, n, i):
                    Primes[j] = 0
        return ret
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = ""
        while n != 0:
            c = str(n & 1)
            ret += c
            n >>= 1
        while len(ret) < 32:
            ret += '0'
        return int(ret, 2)

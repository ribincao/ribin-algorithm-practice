class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        ret = 0

        while n:
            if ret > 1:
                return False
            if n & 1 == 1:
                ret += 1
            n >>= 1
        
        return ret == 1
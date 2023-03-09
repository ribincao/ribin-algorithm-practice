class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        delta = x ^ y
        while delta != 0:
            if delta & 1 ==1:
                ret += 1
            delta >>= 1
        return ret

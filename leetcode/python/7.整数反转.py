class Solution:
    def reverse(self, x: int) -> int:
        ret, sign = 0, 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            x, c = x // 10, x % 10

            ret = ret * 10 + c
            tmp = ret * sign
            if tmp < -(2 ** 31) or tmp > (2 ** 31 - 1):
                return 0
        return sign * ret
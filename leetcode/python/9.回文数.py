class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == self.reverse(x)

    def reverse(self, x: int) -> int:
        ret = 0
        while x:
            x, c = x // 10, x % 10
            ret = ret * 10 + c
        return ret
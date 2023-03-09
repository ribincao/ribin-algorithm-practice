class Solution:
    def addDigits(self, num: int) -> int:

        while num // 10 > 0:
            tmp = 0
            while num != 0:
                num, c = num // 10, num % 10
                tmp += c
            num = tmp
        return num
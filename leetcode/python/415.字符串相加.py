class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == 0: return num2
        if len(num2) == 0: return num1

        ret = ""
        i, j = len(num1) - 1, len(num2) - 1
        c = '0'
        while i >= 0 or j >= 0:
            a = "0"
            if i >= 0:
                a = num1[i]
                i -= 1

            b = "0"
            if j >= 0:
                b = num2[j]
                j -= 1
            tmp, c = self.add(a, b, c)
            ret = tmp + ret
        if c != '0':
            ret = c + ret

        return ret

    def add(self, num1: str, num2: str, c: str) -> Tuple[str, str]:
        num1 = ord(num1) - ord('0')
        num2 = ord(num2) - ord('0')
        c = ord(c) - ord('0')

        ret = num1 + num2 + c
        if ret > 9:
            ret = chr(ret - 10 + ord('0'))
            c = '1'
            return ret, c
        ret = chr(ret + ord('0'))
        c = '0'
        return ret, c
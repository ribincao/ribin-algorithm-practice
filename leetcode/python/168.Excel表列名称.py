class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""
        while columnNumber > 0:

            c = columnNumber % 26
            columnNumber = columnNumber // 26
            if c == 0:
                columnNumber -= 1
                ret = 'Z' + ret
            else:
                ret = chr(c + ord('A') - 1) + ret
        return ret

class Solution:
    def findComplement(self, num: int) -> int:
        ret = ""
        if num == 0:
            return 1
        while num != 0:
            c = num & 1
            if c:
                ret = '0' + ret
            else:
                ret = '1' + ret
            
            num >>= 1
        return int(ret, 2)
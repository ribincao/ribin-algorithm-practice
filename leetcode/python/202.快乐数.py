class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        while n != 0:
            ret = 0
            while n != 0:
                n, c = n // 10, n % 10
                ret += (c * c)
            
            if ret == 1:
                return True
            if ret in store:
                break
            store.add(ret)
            n = ret
        return False
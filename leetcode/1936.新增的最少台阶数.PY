class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n = len(rungs)
        front = 0
        ret = 0
        for i in range(n):
            num = rungs[i]
            if num <= front + dist:
                front = num
                continue
            tmp, c = (num - front) // dist, (num - front) % dist
            if c == 0:
                tmp -= 1
            ret += tmp
            front = num
        return ret


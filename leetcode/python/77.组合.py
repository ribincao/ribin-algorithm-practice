class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        nums = [i for i in range(1, n + 1)]
        if n == k:
            return [nums]
        stop = min(k, n - k)
        def dfs(x = 0):
            if x == stop:
                if x == k:
                    tmp = sorted(nums[:k])
                else:
                    tmp = sorted(nums[n - k:])
                if tmp not in ret:
                    ret.append(tmp)
                return
            for i in range(x, n):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        dfs()
        return ret

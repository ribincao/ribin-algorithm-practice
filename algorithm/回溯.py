# 全排列 -> 回溯 -> 深度优先搜索 -> 递归 -> 栈
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        def dfs(x = 0):
            if x == n:
                ret.append(list(nums))
                return
            
            for i in range(x, n):
                if x != i and nums[x] == nums[i]:
                    continue
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs()
        return ret
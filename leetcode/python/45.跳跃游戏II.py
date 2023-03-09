class Solution:
    def jump(self, nums: List[int]) -> bool:
        """ 贪心算法 """
        goal = len(nums) - 1
        ret = 0
        while goal > 0:
            for i in range(goal):
                if nums[i] + i >= goal:
                    goal = i
                    ret += 1
                    break
        return ret
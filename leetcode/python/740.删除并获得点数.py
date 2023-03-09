class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)
        rob_nums = [0 for _ in range(max_val + 1)]
        for num in nums:
            rob_nums[num] += num
        
        ret = self.rob(rob_nums)
        return ret

    def rob(self, nums: List[int]) -> int:
        i_2, i_1 = 0, 0
        for num in nums:
            i_2, i_1 = i_1, max(num + i_2, i_1)
        return i_1
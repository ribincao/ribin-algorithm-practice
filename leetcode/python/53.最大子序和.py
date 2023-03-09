class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ret = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i - 1], nums[i])
            ret = max(ret, nums[i])
        return ret
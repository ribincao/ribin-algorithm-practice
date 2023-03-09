class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.rob2(nums[: n - 1]), self.rob2(nums[1:]))

    def rob2(self, nums: List[int]) -> int:

        i_1, i_2 = 0, 0
        for num in nums:
            i_2, i_1 = i_1, max(num + i_2, i_1)
        return i_1
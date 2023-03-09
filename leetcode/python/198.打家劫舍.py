class Solution:
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        for i in range(1, len(nums)):
            if i < 2:
                nums[i] = max(nums[i - 1], nums[i])
                continue
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[i]
    
    def rob(self, nums: List[int]) -> int:
        i_1, i_2 = 0, 0
        for num in nums:
            i_1, i_2 = max(num + i_2, i_1), i_1
        return i_1
        
        
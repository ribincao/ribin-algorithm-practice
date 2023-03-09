class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = [1 for _ in range(len(nums))]

        for num in nums:
            if num < len(nums):
                ret[num] = 0
        for i in range(len(ret)):
            if ret[i] == 1:
                return i
        return len(ret)
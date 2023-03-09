class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        Founded = [0 for _ in range(len(nums) + 1)]
        for num in nums:
            Founded[num] = 1
        for i in range(len(Founded)):
            if Founded[i] == 0:
                ret = i
                break
        return ret

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1: return nums

        ret = [1 for _ in range(n)]
        for i in range(1, n):
            ret[i] = ret[i - 1] * nums[i - 1]

        j = n - 2
        tmp = 1
        while j >= 0:
            tmp *= nums[j + 1]
            ret[j] *= tmp
            j -= 1
        
        return ret
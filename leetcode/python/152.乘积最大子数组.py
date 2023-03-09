class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ret = pos = neg = 0
        for i in range(n):
            if nums[i] == 0:
                pos = neg = 0
                continue
            tmp = [pos * nums[i], neg * nums[i], nums[i]]
            pos = max(tmp)
            neg = min(tmp)

            # print(pos, neg, tmp, ret)
            ret = max(pos, ret)
        return ret
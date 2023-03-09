class Solution:

    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        i, j = 0, n - 1
        ret = 0

        while i < j:
            ret = max(ret, nums[i] + nums[j])
            i += 1
            j -= 1
        return ret

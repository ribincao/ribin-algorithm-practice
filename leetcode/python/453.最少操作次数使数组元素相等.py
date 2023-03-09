class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ret = []
        s, n = sum(nums), len(nums)
        for i in range(n):
            num = s - n * nums[i]
            ret.append(num)
        return max(ret)

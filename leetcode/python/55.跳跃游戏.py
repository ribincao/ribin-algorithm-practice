class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ret = [False for _ in range(n)]
        ret[0] = True

        for i in range(n):
            if ret[i] == False:
                break
            if nums[i] + i + 1 >= n:
                return True
            for j in range(i + 1, i + 1 + nums[i]):
                if j + 1 + nums[j] >= n:
                    return True
                ret[j] = True
        return False
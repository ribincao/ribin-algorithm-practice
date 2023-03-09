class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d, ret = dict(), list()
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                ret.append(d[target - nums[i]])
                ret.append(i)
                return ret
        return ret
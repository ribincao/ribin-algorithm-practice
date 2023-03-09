from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        if n == 0: return ret

        nums.sort()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            target = 0 - nums[first]
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                
                if second == third:
                    break
                
                if nums[second] + nums[third] == target:
                    ret.append([nums[first], nums[second], nums[third]])
        return ret


if __name__ == '__main__':
    nums = [-2, -2, -1, -1, 0, 1, 2, 3]
    s = Solution()
    print(s.threeSum(nums))
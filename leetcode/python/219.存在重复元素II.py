class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                delta = i - d[num]
                if delta <= k:
                    return True
            d[num] = i
        return False
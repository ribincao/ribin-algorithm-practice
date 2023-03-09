class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1

        d = set()
        for num in nums:
            d.add(num)
        
        nums = sorted(d)
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]
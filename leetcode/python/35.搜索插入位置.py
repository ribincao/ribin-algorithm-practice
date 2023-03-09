class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + int((end - start) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] >= target:
            return start
        return start + 1
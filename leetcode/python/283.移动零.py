class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while i < n and j < n:

            while i < n:
                if nums[i] == 0:
                    break
                i += 1
            
            while j < n:
                if nums[j] != 0:
                    break
                j += 1
            if i >= n or j >= n:
                break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            j = i
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        self.swap(nums, 0, len(nums) - 1)
        self.swap(nums, 0, k - 1)
        self.swap(nums, k, len(nums) - 1)

        # self.swap(nums, 0, len(nums) - k - 1)
        # self.swap(nums, len(nums) - k, len(nums) - 1)
        # self.swap(nums, 0, len(nums) - 1)
    
    def swap(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
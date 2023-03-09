def quick_sort(nums: List[int], start: int, end: int):
    if start < end:
        mid = nums[start]
        i, j = start, end
        while i < j:
            while i < j and nums[j] >= mid:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] < mid:
                i += 1
            nums[j] = nums[i]
         
        nums[i] = mid
        quick_sort(nums, start, i - 1)
        quick_sort(nums, i + 1, end)
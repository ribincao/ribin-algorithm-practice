from typing import List

class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        def binSearch(start, end):
            if start < end:
                # print(start, end)
                mid = start + int((end - start) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binSearch(start, mid - 1)
                else:
                    return binSearch(mid + 1, end)
            else:
                if start == end and nums[start] == target:
                    return start
                return -1

        ret = binSearch(0, len(nums) - 1)
        return ret

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + int((end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if start == end and nums[start] == target:
            return start
        return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 2
    s = Solution()
    print(s.search2(nums, target))
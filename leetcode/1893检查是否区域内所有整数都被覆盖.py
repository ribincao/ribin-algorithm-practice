class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        founded = []
        for nums in ranges:
            for num in range(nums[0], nums[1] + 1):
                founded.append(num)
        
        for num in range(left, right + 1):
            if num not in founded:
                return False
        return True
class Solution:
    def massage(self, nums: List[int]) -> int:
        i_2, i_1 = 0, 0
        for num in nums:
            i_1, i_2 = max(num + i_2, i_1), i_1
        return i_1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        record = [0 for i in range(len(nums))]
        for num in nums:
            if record[num - 1] == 0:
                record[num - 1] = 1
        ret = []
        for i in range(len(record)):
            if record[i] == 0:
                ret.append(i + 1)
        
        return ret

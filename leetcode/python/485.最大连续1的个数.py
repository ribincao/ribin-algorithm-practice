class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, tmp = 0, 0
        for num in nums:
            if num == 1:
                tmp += 1
            else:
                ret = max(ret, tmp)
                tmp = 0
        
        if tmp > ret:
            return tmp
        return ret
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        k = j
        ret = [0 for i in range(len(nums))]
        while i <= j:
            if i == j:
                ret[k] = nums[i] * nums[i]
                break
            
            if abs(nums[i]) < abs(nums[j]):
                ret[k] = nums[j] * nums[j]
                j -= 1
            else:
                ret[k] = nums[i] * nums[i]
                i += 1
            k -= 1
        
        return ret
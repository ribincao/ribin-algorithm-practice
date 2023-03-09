class NumArray:
    
    def __init__(self, nums: List[int]):
        self.sums = [0]
        ret = 0
        for num in nums:
            ret += num
            self.sums.append(ret)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
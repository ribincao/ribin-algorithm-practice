class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Store = set()
        for num in nums:
            if num in Store:
                return True
            Store.add(num)
        return False

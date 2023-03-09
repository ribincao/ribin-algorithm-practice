class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        d = dict()
        for num in nums1:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        for num in nums2:
            if num in d and d[num] > 0:
                ret.append(num)
                d[num] -= 1
        
        return ret
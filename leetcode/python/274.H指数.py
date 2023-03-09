class Solution:
    def hIndex(self, citations: List[int]) -> int:
        nums = sorted(citations)
        n = len(nums)
        d = dict()
        for i in range(n):
            times = n - i
            if times not in d:
                d[times] = nums[i]
        
        for k, v in d.items():
            if v >= k:
                return k
        return 0
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2 : return 0

        ret = 0
        i, j = 0, n - 1
        while i < j:
            if height[i] < height[j]:
                ret = max(ret, height[i] * (j - i))
                i += 1
            else:
                ret = max(ret, height[j] * (j - i))
                j -= 1
        return ret
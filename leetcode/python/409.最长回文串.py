class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        ret = 0
        for _, v in d.items():
            if v % 2 == 1:
                ret += 1
        if ret == 0:
            return len(s)
        return len(s) - ret + 1
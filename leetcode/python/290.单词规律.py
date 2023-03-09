class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ret = s.split(' ')
        if len(ret) != len(pattern):
            return False
        dp = {}
        ds = {}
        for i in range(len(pattern)):
            c = pattern[i]
            if c not in dp:
                if ret[i] not in ds:
                    dp[c] = ret[i]
                    ds[ret[i]] = c
                else:
                    return False
            else:
                if dp[c] != ret[i]:
                    return False
        return True
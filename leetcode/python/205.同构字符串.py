class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i in range(len(s)):
            c = s[i]
            if c not in ds:
                if t[i] in dt:
                    return False
                ds[c] = t[i]
                dt[t[i]] = c
            else:
                if ds[c] != t[i]:
                    return False
        
        return True

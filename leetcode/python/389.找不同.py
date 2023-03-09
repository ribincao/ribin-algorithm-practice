class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        dd = {}
        for c in s:
            if c not in dd:
                dd[c] = 0
            dd[c] += 1
        
        for k, v in d.items():
            if k not in dd or v > dd[k]:
                return k
        
        return ""
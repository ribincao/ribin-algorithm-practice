class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in ransomNote:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        ret = {}
        for c in magazine:
            if c not in ret:
                ret[c] = 0
            ret[c] += 1
        
        for k, v in d.items():
            if k not in ret or v > ret[k]:
                return False
        return True
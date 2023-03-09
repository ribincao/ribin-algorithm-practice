class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        
        check = {}
        for c in t:
            if c not in check:
                check[c] = 0
            check[c] += 1
        
        for k, v in cnt.items():
            if k not in check or v != check[k]:
                return False
        
        return True
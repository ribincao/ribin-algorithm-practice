class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m  = len(s1), len(s2)
        if n > m:
            return False
        
        cnt = {}
        for c in s1:
            if c not in  cnt:
                cnt[c] = 0
            cnt[c] += 1
        
        check = {}
        for i in range(n):
            c = s2[i]
            if c not in check:
                check[c] = 0
            check[c] += 1
        if check == cnt:
            return True
        
        for i in range(1, m - n + 1):
            a, b = s2[i - 1], s2[i + n - 1]
            check[a] -= 1
            if check[a] == 0:
                check.pop(a)
            if b not in check:
                check[b] = 0
            check[b] += 1

            if check == cnt:
                return True
        
        return False





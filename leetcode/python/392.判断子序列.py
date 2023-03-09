class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(t)):
            c = t[i]
            if c not in dic:
                dic[c] = []
            dic[c].append(i)
        
        ini = -1
        for c in s:
            if c not in dic:
                return False
            sign = True
            for index in dic[c]:
                if index > ini:
                    sign = False
                    ini = index
                    break
            if sign:
                return False
        return True
            
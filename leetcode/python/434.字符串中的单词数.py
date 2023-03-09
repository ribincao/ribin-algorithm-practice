class Solution:
    def countSegments(self, s: str) -> int:
        ss = s.split(' ')
        ret = 0
        for word in ss:
            if len(word) > 0:
                ret += 1
        return ret
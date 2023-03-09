class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        ret = []
        for string in ss:
            ret.append(self.reverseStr(string))
        return ' '.join(ret)

    def reverseStr(self, s: str) -> str:
        ret = ""
        for c in s:
            ret = c + ret
        return ret
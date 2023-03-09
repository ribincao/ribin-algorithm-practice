class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = self.reverseWord(words[i])
        return ' '.join(words)

    def reverseWord(self, s: str):
        ret = ""
        for c in s:
            ret = c + ret
        return ret
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        bl = [c for c in brokenLetters]
        ret = 0
        for word in words:
            for c in word:
                if c in bl:
                    ret += 1
                    break
        return len(words) - ret
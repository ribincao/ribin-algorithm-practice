class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(': 0, '{': 1, '[': 2}
        right = {')': 0, '}': 1, ']': 2}

        stack = []
        for c in s:
            if c in left:
                stack.append(c)
                continue
            if not stack or left[stack[-1]] != right[c]:
                return False
            stack.pop()
        return not stack
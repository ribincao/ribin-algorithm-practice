# 最长无重复子串 -> 滑动窗口 -> 左右指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        Founded = set()

        left, max_len, cur_len = 0, 0, 0
        for right in range(len(s)):
            cur_len += 1
            while s[right] in Founded:
                Founded.remove(s[left])
                cur_len -= 1
                left += 1
            
            if cur_len > max_len:
                max_len = cur_len
            Founded.add(s[right])
        return max_len
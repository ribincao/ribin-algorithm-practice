class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        begin, max_len = 0, 1
        for length in range(2, n + 1):
            for start in range(n):
                end = start + length - 1
                if end >= n:
                    break
                
                if s[start] != s[end]:
                    dp[start][end] = False
                else:
                    if length < 4:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][end - 1]
                
                if dp[start][end] and length > max_len:
                    max_len = length
                    begin = start
        
        return s[begin:begin + max_len]
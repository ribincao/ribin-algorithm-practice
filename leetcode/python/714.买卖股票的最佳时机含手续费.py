class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[-prices[0], 0]] + [[0] * 2 for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][0] + prices[i] - fee, dp[i - 1][1])
        return dp[n - 1][1]
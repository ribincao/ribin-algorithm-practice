class SockBuy:
    
    def __init__(self, prices: List[int], once: bool=False, fee: int=0, cold_time: bool=False):
        self.prices = prices
        self.fee = fee
        self.cold_time = cold_time
        self.once = once

    def run(self):
        if self.cold_time:
            return self.max_profit_with_cold()
        if self.fee > 0:
            return self.max_profit_with_fee()
        if self.once:
            return self.max_profit_with_once()
        return self.max_profit()

    def max_profit(self):
        prices = self.prices
        buy = prices[0]
        ret = 0
        for sell in prices:
            if sell >= buy:
                ret += (sell - buy)
            buy = sell
        return ret

    def max_profit_with_once(self):
        prices = self.prices
        buy = prices[0]
        ret = 0
        for i in range(len(prices)):
            sell = prices[i]
            if sell <= buy:
                buy = sell
            else:
                ret = max(ret, sell - buy)
        return ret

    def max_profit_with_cold(self):
        prices = self.prices
        if not prices:
            return 0

        n = len(prices)
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])

    def max_profit_with_fee(self):
        prices = self.prices
        if not prices:
            return 0
        n = len(prices)
        dp = [[-prices[0], 0]] + [[0] * 2 for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][0] + prices[i] - self.fee, dp[i - 1][1])
        return dp[n - 1][1]
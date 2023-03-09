class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ret = 0
        for sell in prices:
            if sell >= buy:
                ret += (sell - buy)
            buy = sell
        return ret
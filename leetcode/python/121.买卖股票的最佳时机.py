class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret, i, j = 0, 0, 0
        while j < len(prices) - 1:
            if prices[j + 1] > prices[i]:
                ret = max(ret, prices[j + 1] - prices[i])
            else:
                i = j + 1
            
            j += 1
        return ret

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ret = 0
        for i in range(len(prices)):
            sell = prices[i]
            if sell <= buy:
                buy = sell
            else:
                ret = max(ret, sell - buy)
        return ret

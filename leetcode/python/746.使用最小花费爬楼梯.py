class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost)
        for i in range(2, n + 1):
            ret = min(cost[i - 1] ,cost[i - 2])
            if i == n:
                return ret
            cost[i] += ret
            
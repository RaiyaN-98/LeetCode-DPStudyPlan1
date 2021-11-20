class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        dp.append(0)
        dp.append(cost[0])
        n = len(cost)
        for i in range (2, n+1):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i-1])
            
        return min(dp[n-1], dp[n])

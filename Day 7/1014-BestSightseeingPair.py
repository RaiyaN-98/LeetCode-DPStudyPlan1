class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = []
        dp.append(0)
        dp.append(values[0] + values[1] + 0 - 1)
        ans = dp[1]
        for i in range(2, len(values)):
            dp.append(max(dp[i-1] - values[i-1] + i - 1 + values[i] - i, values[i-1] + values[i] - 1))
            ans = max(ans, dp[i])
        
        return ans

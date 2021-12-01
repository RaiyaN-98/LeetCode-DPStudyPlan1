class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        ans = 0
        for x in prices:
            ans = max(ans, x-mn)
            mn = min(x, mn)
        return ans

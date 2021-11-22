class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = []
        dp.append(0)
        currD = nums[0]
        nextJ = nums[0]
        prevP = 0
        nextP = 0
        n = len(nums)
        for i in range(1, n):
            dp.append(dp[prevP] + 1)
            if nextJ < i + nums[i]:
                nextJ = i + nums[i]
                nextP = i
            if i == currD:
                prevP = nextP
                currD = nextJ
        return dp[n-1]

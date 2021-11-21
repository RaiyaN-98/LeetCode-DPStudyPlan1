class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(0)
        dp.append(nums[0])
        dp.append(nums[1])
        for i in range(3, len(nums) + 1):
            dp.append(max(dp[i-2], dp[i-3]) + nums[i-1])
        
        ans = 0
        for x in dp:
            ans = max(x, ans)
            
        return ans

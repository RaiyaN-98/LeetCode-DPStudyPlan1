class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = []
        dp0 = []
        dp1.append(0)
        dp0.append(0)
        dp1.append(nums[0])
        dp0.append(0)
        dp1.append(0)
        dp0.append(nums[1])
        for i in range(3, len(nums) + 1):
            dp1.append(max(dp1[i-2], dp1[i-3]) + nums[i-1])
            dp0.append(max(dp0[i-2], dp0[i-3]) + nums[i-1])
            if i == len(nums):
                dp1[i] -= min(nums[0], nums[i-1])
        ans = 0
        for i in range(len(dp1)):
            ans = max(ans, dp1[i])
            ans = max(ans, dp0[i])
            
        return ans

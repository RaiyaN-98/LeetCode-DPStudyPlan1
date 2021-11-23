class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx = -1000000
        sm = 0
        mnS = 0
        tmS = 0
        arr = []
        tmSP = 0
        mxS = 0
        for i in range(len(nums)):
            tmS = tmS + nums[i]
            if tmS > 0:
                tmS = 0
            mnS = min(tmS, mnS)
            tmSP = tmSP + nums[i]
            if tmSP < 0:
                tmSP = 0
            mxS = max(tmSP, mxS)
            sm += nums[i]
            mx = max(nums[i], mx)
        ans = max(sm - mnS, mxS)
        if mx < 0:
            ans = mx
        
        return ans
        
            

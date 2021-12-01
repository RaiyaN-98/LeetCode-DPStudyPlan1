class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = []
        totProd = []
        lastN = -1
        lastZ = -1
        dp.append(0)
        totProd.append(1)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                dp.append(0)
                lastZ = i
                lastN = -1
                totProd.append(1)
            elif nums[i] < 0:
                if lastN == -1:
                    lastN = i
                totProd.append(totProd[i]*(nums[i]/abs(nums[i])))
                if totProd[i + 1] < 0:
                    dp.append(i-lastN)
                else:
                    dp.append(max(dp[i] + 1, i - lastZ))
            else:
                dp.append(dp[i] + 1)
                totProd.append(totProd[i])
            ans = max(dp[i+1], ans)
        
        return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpM = []
        dpT = []
        fL = 1
        for i in range(len(nums)):
            if i == 0 or nums[i-1] == 0:
                dpT.append(nums[i])
                dpM.append(nums[i])
                fL = 1
            else:
                dpT.append(dpT[i-1]*nums[i])
                if dpT[i] >= int(0):
                    dpM.append(dpT[i])
                else:
                    dpM.append(int(dpT[i]/fL))
            if fL == 1 and nums[i] < 0:
                fL = dpT[i]
        
        mx = dpM[0]
        for x in dpM:
            mx = max(x, mx)
        
        return mx
                
            
